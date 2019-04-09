# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554823390.4737544
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/drug/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'center_column']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def center_column():
            return render_center_column(context._locals(__M_locals))
        prescribers = context.get('prescribers', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        meds = context.get('meds', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Drugs')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def center_column():
            return render_center_column(context)
        meds = context.get('meds', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h3 class="center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( meds.drugname ))
        __M_writer('</h3>\r\n<p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'This drug is an opiate' if meds.isopioid == 1 else 'This drug is not an opiate' ))
        __M_writer('</p>\r\n<br>\r\n<table class="center">\r\n    <tr>\r\n        <td>ID</td>\r\n        <td>Name</td>\r\n        <td>Quantity</td>\r\n    </tr>\r\n')
        for dr in prescribers:
            __M_writer('        <tr>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.doctorid ))
            __M_writer('<br></td>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.lname ))
            __M_writer('<br></td>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.quantity ))
            __M_writer('<br></td>\r\n        </tr>\r\n')
        __M_writer('</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/drug/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "51": 23, "57": 3, "63": 3, "69": 5, "78": 5, "79": 6, "80": 6, "81": 7, "82": 7, "83": 15, "84": 16, "85": 17, "86": 17, "87": 18, "88": 18, "89": 18, "90": 18, "91": 19, "92": 19, "93": 22, "99": 93}}
__M_END_METADATA
"""
