#!/usr/bin/env python3
"""
    Tools for building Voron 2.4 3D Printed part checklist.
"""
import csv
import os
import re

CATEGORY_MAP = {
    "Electronics_Bay": "Electronics Bay",
    "Exhaust_Filter": "Exhaust Filter",
    "Gantry": "Gantry",
    "Panel_Mounting": "Panel Mounting",
    "Skirts": "Skirts",
    "Spool_Management": "Spool Management",
    "Superceded_Parts": "Superceded Parts",
    "Test_Prints": "Test Prints",
    "Tools": "Tools",
    "Z_Drive": "Z-Drive",
    "Z_Endstop": "Z-Endstop",
    "Z_Idlers": "Z-Idlers"
}

FNAME_FILTER = [".DS_Store"]
COLORS = ["Black", "Red"]

def part_cat_name_bldr(fpath):
    fpath = fpath.replace('[a]_','').replace("_", "-")
    fpath = re.sub('[_|\-]x(\d)', '', fpath)

    fparts = fpath.split(os.sep)
    category = fparts[0]
    group = '/'.join(fparts[1:-1])
    part = os.path.splitext(fparts[-1])[0]

    return category, group, part

def record_builder(fpath):
    """
    Part name format
        Derived from STL file name

    Record format:
        category
        part group
        part name
        quantity
        color
        status
        quality
        required
        build Mod
        STL File
        filament
    """
    fparts = fpath.split(os.sep)
    part_fname = fparts[-1]

    category, group, name = part_cat_name_bldr(fpath)

    if part_fname.startswith('[a]'):
        color = COLORS[1]
    else:
        color = COLORS[0]

    quantity = re.findall('[_|\-]x(\d)', part_fname)
    if quantity:
        quantity = int(quantity[0])
    else:
        quantity = 1

    status = "Not Printed"
    quality = ""
    filament = "Prusament ASA"
    required = "YES"
    build_mod = "NO"

    # Mark non-require or parts to exclude
    for filter in ['Superceded', '250', '300', 'Bowden']:
        if filter in fpath:
            quality = 'N/A'
            status = 'DO NOT PRINT'
            required = "NO"
            quantity = 0
    if 'Printheads' in group:
        printhead = fpath.split('/')[-2]
        if printhead in ["Dragon","Dragonfly_BMS","E3D_Revo_Micro","E3D_Revo_Voron","E3D_V6","Slice_Mosquito"]:
            quality = 'N/A'
            status = 'DO NOT PRINT'
            required = "NO"
            quantity = 0

    #return f"{category},{group},{name},{color},{status},{quality},{required},{build_mod},{fpath},{filament}"
    return [category,group,name,quantity,color,status,quality,required,build_mod,fpath,filament]

def build_part_list(fpath: str = "/Users/cwilder/Documents/3D Printing/cee-wals/voron-2.4/STLs"):
    """
    Usage:
        data = build_part_list()
    """
    os.chdir(fpath)
    data = list()
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("."):
        for fname in files:
            if fname not in FNAME_FILTER:
                fpath = os.path.join(root[2:], fname)
                data.append(record_builder(fpath))
    return data

def create_csv_file(data, fname:str = '/Users/cwilder/Documents/3D Printing/cee-wals/voron-2.4/custom/scripts/voron_part_checklist_data.csv'):
    """
    usage:
        data = build_part_list("/Users/cwilder/Documents/3D Printing/cee-wals/voron-2.4/STLs")
        create_csv_file(data, '/Users/cwilder/Documents/3D Printing/cee-wals/voron-2.4/custom/scripts/voron_part_checklist_data.csv')
    """
    with open(fname, 'w') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerows(data)

def get_categories():
    """
    Usage:
        cats, sub_cats = get_categories()
    """
    cats = set()
    sub_cats = set()
    for root, dirs, files in os.walk('.'):
        fpath = root[2:]
        fparts = fpath.split(os.sep)
        if fparts[0]:
            if len(fparts) == 1:
                cats.add(fparts[0])
            else:
                sub_cats.add('/'.join(fparts))
    return list(cats), list(sub_cats)
