# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554788686.8685899
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/drug/templates/top10.html'
_template_uri = 'top10.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['top10']


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
    return runtime._inherit_from(context, 'index.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top10():
            return render_top10(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top10'):
            context['self'].top10(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top10(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top10():
            return render_top10(context)
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        drug = context.get('drug', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3 class="center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drug ))
        __M_writer('</h3>\r\n    <br>\r\n    <table class="center">\r\n    <tr>\r\n        <td>ID</td>\r\n        <td>Name</td>\r\n        <td>Quantity</td>\r\n    </tr>\r\n')
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
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/drug/templates/top10.html", "uri": "top10.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 20, "50": 3, "59": 3, "60": 4, "61": 4, "62": 12, "63": 13, "64": 14, "65": 14, "66": 15, "67": 15, "68": 15, "69": 15, "70": 16, "71": 16, "72": 19, "78": 72}}
__M_END_METADATA
"""
