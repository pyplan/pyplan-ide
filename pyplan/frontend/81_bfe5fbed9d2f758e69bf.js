/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[81,5],{1030:function(n,t,o){var a=o(690);function e(n){return n&&(n.__esModule?n.default:n)}n.exports=(a.default||a).template({compiler:[8,">= 4.3.0"],main:function(n,t,a,l,i){var s=null!=t?t:n.nullContext||{},r=n.escapeExpression,c=n.lambda;return'<div class="">\n\n    <table class="table">\n        <tr>\n            <td>\n                <span>'+r(e(o(688)).call(s,"from",{name:"L",hash:{},data:i,loc:{start:{line:6,column:22},end:{line:6,column:34}}}))+'</span>\n            </td>\n            <td class="col-sm-4">\n                <input type="text" class="form-control cf_from" value="'+r(c(null!=t?t.from:t,t))+'">\n            </td>\n            <td>\n                <span>'+r(e(o(688)).call(s,"to",{name:"L",hash:{},data:i,loc:{start:{line:12,column:22},end:{line:12,column:32}}}))+'</span>\n            </td>\n            <td class="col-sm-4">\n                <input type="text" class="form-control cf_to" value="'+r(c(null!=t?t.to:t,t))+'">\n            </td>\n        </tr>\n\n        <tr>\n            <td>\n                <span>'+r(e(o(688)).call(s,"color_and_size",{name:"L",hash:{},data:i,loc:{start:{line:21,column:22},end:{line:21,column:44}}}))+'</span>\n            </td>\n            <td>\n\n                <input type="text" class="font-color spectrum-colors" value="#000" style="display:none;" />\n\n                <div class="format-separator"></div>\n\n                <select class="mini-selector input-small font-selector">\n                    <option value="8">8</option>\n                    <option value="9">9</option>\n                    <option value="10">10</option>\n                    <option value="11">11</option>\n                    <option value="12">12</option>\n                    <option value="13" selected>13</option>\n                    <option value="14">14</option>\n                    <option value="15">15</option>\n                    <option value="16">16</option>\n                    <option value="17">17</option>\n                    <option value="18">18</option>\n                    <option value="19">19</option>\n                    <option value="20">20</option>\n                    <option value="25">25</option>\n                    <option value="30">30</option>\n                </select>\n\n\n            </td>\n\n            <td>\n                <span>'+r(e(o(688)).call(s,"font_style",{name:"L",hash:{},data:i,loc:{start:{line:51,column:22},end:{line:51,column:40}}}))+'</span>\n            </td>\n            <td>\n                <button class="btn bold format-button" data-format-key="Bold"><i class="fa fa-bold"></i></button>\n                <button class="btn italic format-separator format-button" data-format-key="Italic"><i\n                        class="fa fa-italic"></i></button>\n                <button class="btn underline format-separator format-button" data-format-key="Underline"><i\n                        class="fa fa-underline"></i></button>\n            </td>\n        </tr>\n\n        <tr>\n            <td>\n                <span>'+r(e(o(688)).call(s,"background",{name:"L",hash:{},data:i,loc:{start:{line:64,column:22},end:{line:64,column:40}}}))+'</span>\n            </td>\n            <td>\n                <input type="text" class="background-color spectrum-colors" value="#fff" style="display:none;" />\n            </td>\n\n            <td>\n                <span>'+r(e(o(688)).call(s,"shapes",{name:"L",hash:{},data:i,loc:{start:{line:71,column:22},end:{line:71,column:36}}}))+'</span>\n            </td>\n            <td>\n                <select class="input-small position-selector">\n                    <option value="right">'+r(e(o(688)).call(s,"_right",{name:"L",hash:{},data:i,loc:{start:{line:75,column:42},end:{line:75,column:56}}}))+'</option>\n                    <option value="left">'+r(e(o(688)).call(s,"_left",{name:"L",hash:{},data:i,loc:{start:{line:76,column:41},end:{line:76,column:54}}}))+'</option>\n                    <option value="shape">'+r(e(o(688)).call(s,"only_shape",{name:"L",hash:{},data:i,loc:{start:{line:77,column:42},end:{line:77,column:60}}}))+'</option>\n                </select>\n\n                <div class="format-separator"></div>\n\n                <select class=\'select2-me input-small shape-selector\' style="min-width: 70px;">\n                    <option value="none">'+r(e(o(688)).call(s,"none",{name:"L",hash:{},data:i,loc:{start:{line:83,column:41},end:{line:83,column:53}}}))+'</option>\n                    <option value="fa fa-circle"></option>\n                    <option value="far fa-circle"></option>\n                    <option value="fa fa-check"></option>\n                    <option value="fa fa-check-square-o"></option>\n                    <option value="fa fa-arrow-down"></option>\n                    <option value="fa fa-arrow-up"></option>\n                    <option value="fa fa-arrow-right"></option>\n\n                    <option value="fa fa-flag"></option>\n                    <option value="far fa-flag"></option>\n                    <option value="fa fa-square"></option>\n                    <option value="far fa-square"></option>\n                    <option value="fa fa-star"></option>\n                    <option value="far fa-star"></option>\n                    <option value="fa fa-caret-down"></option>\n                    <option value="fa fa-caret-up"></option>\n\n                    <option value="fa cub-triangle-down"></option>\n                    <option value="fa cub-triangle-up"></option>\n\n                    <option value="fa fa-chevron-down"></option>\n                    <option value="fa fa-chevron-up"></option>\n                </select>\n            </td>\n        </tr>\n\n        <tr>\n            <td>\n                <span>'+r(e(o(688)).call(s,"link_to_dashboard",{name:"L",hash:{},data:i,loc:{start:{line:112,column:22},end:{line:112,column:47}}}))+'</span>\n            </td>\n            <td colspan="3">\n                <select class="select2-me dashboardLinked" data-key="dashboard_link" style="width:175px;">\n                </select>\n\n                <div class="format-separator"></div>\n\n                <select class="input-small target-selector" style="width:175px;">\n                    <option value="_self">'+r(e(o(688)).call(s,"close_current",{name:"L",hash:{},data:i,loc:{start:{line:121,column:42},end:{line:121,column:63}}}))+'</option>\n                    <option value="_blank">'+r(e(o(688)).call(s,"open_new",{name:"L",hash:{},data:i,loc:{start:{line:122,column:43},end:{line:122,column:59}}}))+'</option>\n                </select>\n\n            </td>\n        </tr>\n\n\n\n    </table>\n\n    <input name="current_format_item" type="hidden" value="'+r(c(null!=t?t.pos:t,t))+'" />\n\n\n</div>'},useData:!0})},683:function(n,t,o){"use strict";(function(a){var e;void 0===(e=function(){return a.Controller.extend({name:"showModal",show:function(n){Promise.all([o.e(2),o.e(120)]).then(function(){var t=[o(700)];(function(t){(new t).render(n)}).apply(null,t)}).catch(o.oe)}})}.apply(t,[]))||(n.exports=e)}).call(this,o(694))},826:function(n,t,o){"use strict";(function(a,e){var l,i,s=o(18);function r(n,t,o){return t in n?Object.defineProperty(n,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):n[t]=o,n}l=[o(683),o(1030)],void 0===(i=function(n,t){return a.View.extend({el:e("body"),render:function(a,l){var i=t(l);(new n).show({title:(0,s.translate)("conditional_format"),html:i,modalClass:"conditional-format-popup",buttons:[{title:(0,s.translate)("yes"),css:"primary",code:"yes"},{title:(0,s.translate)("cancel"),code:"cancel"}],callback:function(n){if("yes"==n){var t=e("#main-modal input.cf_from"),o=e("#main-modal input.cf_from").val();if(""==o)return t.focus(),!1;var l=e("#main-modal input.cf_to"),i=e("#main-modal input.cf_to").val();if(""==i)return l.focus(),!1;var s=e('#main-modal input[name="current_format_item"]').val(),c=e("#main-modal input.font-color").val(),u=e("#main-modal input.background-color").val(),d=e("#main-modal select.dashboardLinked"),p=d.val(),f=function(n){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{},a=Object.keys(o);"function"==typeof Object.getOwnPropertySymbols&&(a=a.concat(Object.getOwnPropertySymbols(o).filter(function(n){return Object.getOwnPropertyDescriptor(o,n).enumerable}))),a.forEach(function(t){r(n,t,o[t])})}return n}({pos:""!=s&&parseInt(s)>=0?s:-1,from:o,to:i},""==c?null:{fontColor:c},""==u?null:{backgroundColor:u},{fontSize:e("#main-modal select.font-selector").val(),shape:e("#main-modal select.shape-selector").val(),shapePosition:e("#main-modal select.position-selector").val(),fontBold:e('#main-modal button.format-button[data-format-key="Bold"]').hasClass("btn-inverse"),fontItalic:e('#main-modal button.format-button[data-format-key="Italic"]').hasClass("btn-inverse"),fontUnderline:e('#main-modal button.format-button[data-format-key="Underline"]').hasClass("btn-inverse")},p&&"-1"!=p?{dashboardId:p,dashboardName:d.select2("data").text,target:e("#main-modal select.target-selector").val()}:{dashboardId:void 0,dashboardName:void 0,target:void 0}),m=a.getView();m&&m.updateTableConditionalFormat(f)}},onLoad:function(n){var t=n.find("input.font-color");t.colorPicker(),l&&l.hasOwnProperty("fontColor")&&t.spectrum("set",l.fontColor);var a=n.find("input.background-color");a.colorPicker(),l&&l.hasOwnProperty("backgroundColor")&&a.spectrum("set",l.backgroundColor);var i=function(n){return"none"==n.id?n.text:"<i class='".concat(n.id,"'></i>")},s=n.find(".select2-me");s.select2({minimumResultsForSearch:-1,formatResult:i,formatSelection:i,escapeMarkup:function(n){return n}}),l&&l.hasOwnProperty("shape")&&s.select2("val",l.shape);var r=n.find(".position-selector");r.select2({minimumResultsForSearch:-1}),l&&l.hasOwnProperty("shapePosition")&&r.select2("val",l.shapePosition),l&&l.hasOwnProperty("fontSize")&&n.find(".font-selector").val(l.fontSize),n.find("button.format-button").on("click",function(){e(this).toggleClass("btn-inverse")}),l&&l.hasOwnProperty("fontBold")&&l.fontBold&&e('#main-modal button.format-button[data-format-key="Bold"]').addClass("btn-inverse"),l&&l.hasOwnProperty("fontItalic")&&l.fontItalic&&e('#main-modal button.format-button[data-format-key="Italic"]').addClass("btn-inverse"),l&&l.hasOwnProperty("fontUnderline")&&l.fontUnderline&&e('#main-modal button.format-button[data-format-key="Underline"]').addClass("btn-inverse");var c=n.find("select.dashboardLinked");c.hasClass("select2-offscreen")&&c.select2("destroy"),c.select2({minimumResultsForSearch:1,escapeMarkup:function(n){return n}}),o.e(13).then(function(){var n=[o(740)];(function(n){(new n).show(c,{addNoneOption:!0,complete:function(){l&&l.hasOwnProperty("dashboardId")&&c.select2("val",l.dashboardId)}})}).apply(null,n)}).catch(o.oe);var u=n.find(".target-selector");u.select2({minimumResultsForSearch:-1}),l&&l.hasOwnProperty("target")&&u.select2("val",l.target)},onClose:function(n){n.find(".spectrum-colors").each(function(n,t){e(this).spectrum("destroy")}),n.find("select").each(function(n,t){e(this).data("select2")&&e(this).select2("destroy")})}})}})}.apply(t,l))||(n.exports=i)}).call(this,o(218),o(1))}}]);