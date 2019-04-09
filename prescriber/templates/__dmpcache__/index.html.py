# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554826631.736905
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/prescriber/templates/index.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        dr = context.get('dr', UNDEFINED)
        medications = context.get('medications', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
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
        __M_writer('Prescribers')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        dr = context.get('dr', UNDEFINED)
        medications = context.get('medications', UNDEFINED)
        def center_column():
            return render_center_column(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n    <h3>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.fname ))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.lname ))
        __M_writer('</h3>  \r\n    <br>\r\n        <div class="row">\r\n            <div class="col"> \r\n                <table>\r\n                    <tr>\r\n                        <td>Gender:</td>\r\n                        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.gender ))
        __M_writer('</td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>Credentials:</td>\r\n                        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.credentials ))
        __M_writer('</td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>Location:</td>\r\n                        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.state ))
        __M_writer('</td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>Specialty:</td>\r\n                        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( dr.specialty ))
        __M_writer('</td>\r\n                    </tr>\r\n                </table>\r\n            </div>\r\n            <div class="col">\r\n                <div class="drugsprescribed">\r\n                    <table>\r\n                        <tr>\r\n                            <td>Drug Name</td>\r\n                            <td>Quantity Ordered</td>\r\n                        </tr>\r\n')
        for m in medications:
            __M_writer('                            <tr>\r\n                                <td><a href="/drug/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( m.drug ))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( m.drug ))
            __M_writer('</a></td>\r\n                                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( m.qty ))
            __M_writer('</td>\r\n                            </tr>\r\n')
        __M_writer('                    </table>\r\n                </div>\r\n            </div>\r\n        </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/INTEX/website/website/prescriber/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "51": 48, "57": 3, "63": 3, "69": 5, "78": 5, "79": 7, "80": 7, "81": 7, "82": 7, "83": 14, "84": 14, "85": 18, "86": 18, "87": 22, "88": 22, "89": 26, "90": 26, "91": 37, "92": 38, "93": 39, "94": 39, "95": 39, "96": 39, "97": 40, "98": 40, "99": 43, "105": 99}}
__M_END_METADATA
"""
