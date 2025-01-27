import xml.etree.ElementTree as ET
from roster import Cost, Category, Profile, Rule, Selection, Force, Roster, Characteristic
import pdb

namespace = {'ns': 'http://www.battlescribe.net/schema/rosterSchema'}

def parse_costs(costs_element):
    costs = []
    if costs_element is not None:
        for cost in costs_element.findall('ns:cost', namespace):
            costs.append(Cost(cost.get('name'), cost.get('typeId'), float(cost.get('value'))))
    return costs

def parse_categories(categories_element):
    categories = []
    if categories_element is not None:
        for category in categories_element.findall('ns:category', namespace):
            categories.append(Category(category.get('id'), category.get('name'), category.get('entryId'), category.get('primary') == 'true'))
    return categories

def parse_characteristics(characteristics_element):
    characteristics = []
    if characteristics_element is not None:
        for characteristic in characteristics_element.findall('ns:characteristic', namespace):
            characteristics.append(Characteristic(characteristic.get('name'), characteristic.get('typeId'), characteristic.text))
    return characteristics

def parse_profile(profile_element):
    profile = Profile(profile_element.get('id'), profile_element.get('name'), profile_element.get('hidden') == 'false', profile_element.get('typeId'), profile_element.get('typeName'))
    profile.characteristics = parse_characteristics(profile_element.find('ns:characteristics', namespace))
    return profile

def parse_profiles(profiles_element):
    profiles = []
    if profiles_element is not None:
        for profile in profiles_element.findall('ns:profile', namespace):
            profiles.append(parse_profile(profile))
    return profiles

def parse_rules(rules_element):
    rules = []
    if rules_element is not None:
        for rule in rules_element.findall('ns:rule', namespace):
            rules.append(Rule(rule.get('id'), rule.get('name'), rule.get('publicationId'), rule.get('page'), rule.get('hidden') == 'false'))
    return rules

def parse_selections(selections_element):
    selections = []
    if selections_element is not None:
        for selection in selections_element.findall('ns:selection', namespace):
            sel = Selection(selection.get('id'), selection.get('name'), selection.get('entryId'), int(selection.get('number')), selection.get('type'))
            sel.rules = parse_rules(selection.find('ns:rules', namespace))
            sel.profiles = parse_profiles(selection.find('ns:profiles', namespace))
            sel.costs = parse_costs(selection.find('ns:costs', namespace))
            sel.categories = parse_categories(selection.find('ns:categories', namespace))
            sel.selections = parse_selections(selection.find('ns:selections', namespace))
            selections.append(sel)
    return selections

def parse_forces(forces_element):
    forces = []
    for force in forces_element.findall('ns:force', namespace):
        f = Force(force.get('id'), force.get('name'), force.get('entryId'), force.get('catalogueId'), force.get('catalogueRevision'), force.get('catalogueName'))
        f.rules = parse_rules(force.find('ns:rules', namespace))
        f.selections = parse_selections(force.find('ns:selections', namespace))
        f.costs = parse_costs(force.find('ns:costs', namespace))
        f.categories = parse_categories(force.find('ns:categories', namespace))
        forces.append(f)
    return forces

def parse_roster(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    roster = Roster(root.get('id'), root.get('name'), root.get('battleScribeVersion'), root.get('gameSystemId'), root.get('gameSystemName'), root.get('gameSystemRevision'))
    roster.costs = parse_costs(root.find('ns:costs', namespace))
    roster.forces = parse_forces(root.find('ns:forces', namespace))
    return roster

