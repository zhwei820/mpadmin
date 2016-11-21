# coding=utf-8
import datetime

from item.models import ItemCategory, Item
import re

_valid_fields = {
    'string': {
        "required": r'^(True)|(False)$',
        "default": r'^.*$',
        "valid_rule": r'^(none)|(IPaddress)|(email)|(phone)$',
        "max_length": r'^\d+$',
        'min_length': r'^\d+$',
    },  # 单行文本
    'text': {
        "required": r'^(True)|(False)$',
        "default": r'^(.|\n)*$',
        "valid_rule": r'^(none)|(IPaddress)|(email)|(phone)$',
        "max_length": r'^\d+$',
        'min_length': r'^\d+$',
    },  # 多行文本
    'select': {
        "required": r'^(True)|(False)$',
        "choice": r'^\d+\[(.+)(\|(.+))*\]$',
        "selected": r'^(.+)$'
    },  # 单选
    'multiple_select': {
        "required": r'^(True)|(False)$',
        "choice": r'^\d+\[(.+)(\|(.+))*\]$',
        "selected": r'^(.+)(\|(.+))*$'
    },  # 多选
    'integer': {
        "required": r'^(True)|(False)$',
        "default": r'^\d+$',
        "unit": r'^.+$',
        "max_value": r'^\d+$',
        "min_value": r'^\d+$',
    },  # 整数
    'datetime': {
        "required": r'^(True)|(False)$',
        "default": r'^\d{14}$',
    },  # 时间
    'reference': {
        "required": r'^(True)|(False)$',
        "reference": r'^\w{24}$',
    },  # 引用
    'image': {
        "required": r'^(True)|(False)$',
    },  # 图片
}


def validate_item_field(attr_value, attr_form):
    """
    :param attr_value: item的属性
    :param attr_form: item category的属性规则
    :return:
    """
    if not isinstance(attr_form, dict):
        return -1, {"error": "attr_form is not a dict."}
    required = attr_form.get('required')
    if required == 'false':
        return 0, {"msg": "success"}
    field = attr_form.get('field')
    if not field:
        return -1, {"error": "field missed."}
    if field == "string":
        if not isinstance(attr_value, str):
            return -1, {"error": "attr_value is not a string."}
        if len(attr_value) < attr_form.get('min_length') or len(attr_value) > attr_form.get("max_length"):
            return -1, {"error": "string length invalid."}
        if attr_form.get('valid_rule') == "None":
            return 0, {"msg": "success"}
        elif attr_form.get('valid_rule') == "IPaddress":
            pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')  # 匹配IP地址有待改进
        elif attr_form.get('valid_rule') == "email":
            pattern = re.compile(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$')
        elif attr_form.get('valid_rule') == "phone":
            pattern = re.compile(r'^\d{11}$')
        else:
            return -1, {"error": "invalid valid_rule."}
        match = pattern.match(attr_value)
        if not match:
            return -1, {"error": "did not match rule: %s" % attr_form.get('valid_rule')}
        if len(attr_value) < int(attr_form["min_length"]) or len(attr_value) > int(attr_form["max_length"]):
            return -1, {"error": "invalid string length."}
    elif field == "text":
        if not isinstance(attr_value, str):
            return -1, {"error": "attr_value is not a string."}
        if len(attr_value) < attr_form.get('min_length') or len(attr_value) > attr_form.get("max_length"):
            return -1, {"error": "string length invalid."}
        if attr_form.get('valid_rule') == "None":
            return 0, {"msg": "success"}
        elif attr_form.get('valid_rule') == "IPaddress":
            pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')  # 匹配IP地址有待改进
        elif attr_form.get('valid_rule') == "email":
            pattern = re.compile(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$')
        elif attr_form.get('valid_rule') == "phone":
            pattern = re.compile(r'^\d{11}$')
        else:
            return -1, {"error": "invalid valid_rule."}
        match = pattern.match(attr_value)
        if not match:
            return -1, {"error": "did not match rule: %s" % attr_form.get('valid_rule')}
        if len(attr_value) < int(attr_form["min_length"]) or len(attr_value) > int(attr_form["max_length"]):
            return -1, {"error": "invalid string length."}
    elif field == "select":
        if not isinstance(attr_value, str):
            return -1, {"error": "attr_value is not a dict."}
        if attr_value not in attr_form["choice"][1:-1].split("|"):
            return -1, {"error": "invalid choice."}
    elif field == "multiple_select":
        if not isinstance(attr_value, str):
            return -1, {"error": "attr_value is not a dict."}
        for each in attr_value.split("|"):
            if each not in attr_form["choice"][1:-1].split("|"):
                return -1, {"error": "invalid choice."}
    elif field == "integer":
        if not isinstance(attr_value, int):
            return -1, {"error": "attr_value is not a integer."}
        if attr_value < int(attr_form["min_value"]) or attr_value > int(attr_form["max_value"]):
            return -1, {"error": "invalid integer value."}
    elif field == "datetime":
        if not isinstance(attr_value, str):
            return -1, {"error": "attr_value is not a string."}
        try:
            date_object = datetime.datetime.strptime(attr_value, '%Y%m%d%H%M%S')
        except ValueError:
            return -1, {"error": "time data '%s' does not match format" % attr_value}
    elif field == "reference":
        if not isinstance(attr_value, str):
            return -1, {"error": "attr_value is not a string."}
        item_obj = Item.objects(id=attr_value)
        if not item_obj:
            return -1, {"error": "unknown item."}
        if item_obj.category.id != attr_form["reference"]:
            return -1, {"error": "wrong category."}

    return 0, {"msg": "success"}


def validate_item_structure(data):
    """
    :param data: 待验证的Item数据，是一个dict
    :return:
    """
    if not isinstance(data, dict):
        return -1, {"error": "Data is not a dict."}
    category = data.get("category")
    if not category:
        return -1, {"error": "Category is not defined."}
    field_data = data.get("structure")
    if not field_data:
        return -1, {"error": "Field data are not defined."}
    item_category_object = ItemCategory.objects.get(id=category)
    if item_category_object:
        return -1, {"error": "Category does not exists."}
    for attr_group_name, attr_group_value in field_data:
        if attr_group_name not in item_category_object.structure:
            return -1, {"error": "Invaild attr_group:%s" % attr_group_name}
        for attr_name, attr_value in attr_group_value:
            if attr_name not in item_category_object.structure[attr_group_name]:
                return -1, {"error": "Invaild attr:%s" % attr_name}
            state, msg = validate_item_field(attr_value, item_category_object.structure[attr_group_name][attr_name])
            if state != 0:
                return state, msg
    return 0, {"msg": "success"}


def validate_category_structure(raw_data):
    structure = raw_data.get("structure")
    if not structure:
        return -1, {"error": "raw Data missed attr: structure"}
    if not isinstance(structure, dict):
        return -1, {"error": "structure is not a dict."}
    for k, s_data in structure.items():
        if not isinstance(s_data, dict):
            return -1, {"error": "s_data %s is not a dict." % k}
        for attr_name, data in s_data.items():
            if not isinstance(data, dict):
                return -1, {"error": "Data is not a dict."}
            field = data.get("field")
            if field not in _valid_fields:
                return -1, {"error": "Unknown attribute type."}
            for k, v in _valid_fields[field].items():
                if k not in data:
                    return -1, {"error": "missed rule for %s." % k}
                pattern = re.compile(v)
                match = pattern.match(data[k])
                if not match:
                    return -1, {"error": "dooe not match rule: %s." % k}
            if field == 'string':
                if int(data["min_length"]) > int(data["max_length"]):
                    return -1, {"error": "string: min_length is greater than max_length"}
                if len(data["default"]) < int(data["min_length"]) or len(data["default"]) > int(data["max_length"]):
                    return -1, {"error": "default value's length is invalid"}
            elif field == 'text':
                if int(data["min_length"]) > int(data["max_length"]):
                    return -1, {"error": "string: min_length is greater than max_length"}
                if len(data["default"]) < int(data["min_length"]) or len(data["default"]) > int(data["max_length"]):
                    return -1, {"error": "default value's length is invalid"}
            elif field == 'select':
                choices = data["choice"][1:-1].split("|")
                if data["selected"] not in choices:
                    return -1, {"error": "default choice is not in given choices."}
            elif field == 'multiple_select':
                choices = data["choice"][1:-1].split("|")
                default_choices = data["selected"].split("|")
                for each in default_choices:
                    if each not in choices:
                        return -1, {"error": "default choice is not in given choices."}
            elif field == 'integer':
                if int(data["min_value"]) > int(data["max_value"]):
                    return -1, {"error": "integer: min_value is greater than max_value"}
                if int(data["default"]) < int(data["min_length"]) or int(data["default"]) > int(data["max_length"]):
                    return -1, {"error": "default value is invalid"}
            elif field == 'integer':
                try:
                    date_object = datetime.datetime.strptime(data["default"], '%Y%m%d%H%M%S')
                except ValueError:
                    return -1, {"error": "time data '%s' does not match format" % data["default"]}
            elif field == 'reference':
                item_category_obj = ItemCategory.objects(id=field["reference"])
                if not item_category_obj:
                    return -1, {"error": "unknown reference."}

    return 0, {"msg": "success"}
