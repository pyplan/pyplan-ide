ace.define("ace/theme/cubeplan",
  ["require", "exports", "module", "ace/lib/dom"],
  function (require, exports, module) {
    exports.isDark = false;
    exports.cssClass = "ace-cubeplan";
    exports.cssText = ".ace-cubeplan .ace_gutter {\
    background: #ebebeb;\
    color: #333\
    }\
    .ace-cubeplan .ace_print-margin {\
    width: 1px;\
    background: #e8e8e8\
    }\
    .ace-cubeplan {\
    background-color: #FFFFFF;\
    color: #000000\
    }\
    .ace-cubeplan .ace_cursor {\
    color: #000000\
    }\
    .ace-cubeplan .ace_marker-layer .ace_selection {\
    background: #BDD5FC\
    }\
    .ace-cubeplan.ace_multiselect .ace_selection.ace_start {\
    box-shadow: 0 0 3px 0px #FFFFFF;\
    }\
    .ace-cubeplan .ace_marker-layer .ace_step {\
    background: rgb(255, 255, 0)\
    }\
    .ace-cubeplan .ace_marker-layer .ace_bracket {\
    margin: -1px 0 0 -1px;\
    border: 1px solid #BFBFBF;\
    background-color: #EAEAEA;\
    }\
    .ace-cubeplan .ace_marker-layer .ace_active-line {\
    background: #FFFBD1\
    }\
    .ace-cubeplan .ace_gutter-active-line {\
    background-color : #dcdcdc\
    }\
    .ace-cubeplan .ace_marker-layer .ace_selected-word {\
    border: 1px solid #BDD5FC\
    }\
    .ace-cubeplan .ace_invisible {\
    color: #BFBFBF\
    }\
    .ace-cubeplan .ace_meta,\
    .ace-cubeplan .ace_support.ace_constant.ace_property-value {\
    color: #AF956F\
    }\
    .ace-cubeplan .ace_constant.ace_language {\
    color: #39946A\
    }\
    .ace-cubeplan .ace_constant.ace_numeric {\
    color: #46A609\
    }\
    .ace-cubeplan .ace_constant.ace_character.ace_entity {\
    color: #BF78CC\
    }\
    .ace-cubeplan .ace_invalid {\
    background-color: #FF002A\
    }\
    .ace-cubeplan .ace_fold {\
    background-color: #AF956F;\
    border-color: #000000\
    }\
    .ace-cubeplan .ace_storage,\
    .ace-cubeplan .ace_support.ace_class,\
    .ace-cubeplan .ace_support.ace_function,\
    .ace-cubeplan .ace_support.ace_other,\
    .ace-cubeplan .ace_support.ace_type {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_string {\
    color: #5D90CD\
    }\
    .ace-cubeplan .ace_comment {\
    color: #ABB3B5\
    }\
    .ace-cubeplan .ace_entity.ace_name.ace_tag,\
    .ace-cubeplan .ace_entity.ace_other.ace_attribute-name {\
    color: #606060\
    }\
    .ace-cubeplan .ace_activex {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_alias {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_attribute {\
    color: #795548\
    }\
    .ace-cubeplan .ace_button {\
    color: #687687\
    }\
    .ace-cubeplan .ace_chance {\
    color: #06960E\
    }\
    .ace-cubeplan .ace_command {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_constant {\
    color: #F44336\
    }\
    .ace-cubeplan .ace_constraint {\
    color: #E91E63\
    }\
    .ace-cubeplan .ace_decision {\
    color: #06960E\
    }\
    .ace-cubeplan .ace_determ {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_excelworkbook {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_form {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_formnode {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_function {\
    color: #CB82D8\
    }\
    .ace-cubeplan .ace_graphstyletemplate {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_index {\
    color: #9C27B0\
    }\
    .ace-cubeplan .ace_keyword {\
    color: #AF956F\
    }\
    .ace-cubeplan .ace_library {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_linklibrary {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_linkmodule {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_localvar {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_model {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_module {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_object {\
    color: #F90606\
    }\
    .ace-cubeplan .ace_objective {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_picture {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_pluginfunction {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_pluginlibrary {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_sysfunction {\
    color: #8D19A0\
    }\
    .ace-cubeplan .ace_syslibrary {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_sysvar {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_text {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_variable {\
    color: #C52727\
    }\
    .ace-cubeplan .ace_indent-guide {\
    background: url(\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==\") right repeat-y\
    }";

    var dom = require("../lib/dom");
    dom.importCssString(exports.cssText, exports.cssClass);
  });
