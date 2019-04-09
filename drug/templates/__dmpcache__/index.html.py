# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554788608.2340462
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/drug/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'center_column', 'top10']


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
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def top10():
            return render_top10(context._locals(__M_locals))
        instance = context.get('instance', UNDEFINED)
        def center_column():
            return render_center_column(context._locals(__M_locals))
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
        def top10():
            return render_top10(context)
        instance = context.get('instance', UNDEFINED)
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="row">\r\n            <div class="col">\r\n                <div class="druglist">\r\n                    <table>\r\n                        <tr>\r\n                            <td><b>Drug</b></td>\r\n                            <td><b>Opioid?</b></td>\r\n                        </tr>\r\n')
        for item in instance:
            __M_writer('                        <tr class="druginstance">\r\n                            <td class="pointer" onclick="window.location.href=\'/drug/top10/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.drugname ))
            __M_writer('\'">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.drugname ))
            __M_writer(' <br></td>\r\n                            <td class="center">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Yes' if item.isopioid == 1 else 'No' ))
            __M_writer(' <br></td>\r\n                        </tr>\r\n')
        __M_writer('                    </table>\r\n                </div>\r\n            </div>\r\n\r\n            <div class="col">\r\n                   ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top10'):
            context['self'].top10(**pageargs)
        

        __M_writer(' \r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top10(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top10():
            return render_top10(context)
        __M_writer = context.writer()
        __M_writer('\r\n                   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/drug/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 32, "58": 3, "64": 3, "70": 5, "80": 5, "81": 15, "82": 16, "83": 17, "84": 17, "85": 17, "86": 17, "87": 18, "88": 18, "89": 21, "94": 27, "100": 26, "106": 26, "112": 106}}
__M_END_METADATA
"""
