/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[180],{1067:function(n,t,a){"use strict";(function(e,l){var o,i,c=a(18),d=a(732);o=[a(220),a(1265),a(1266)],void 0===(i=function(n,t,a){return e.View.extend({el:l("#main"),render:function(){var a=this;this.$el.append(t({title:this.options.title,max_height:"".concat(l(window).height()-260,"px")}));var e=l("#wizardSetDataframeIndex"),o=e.find(".commandButtons button"),i=e.find(".modal-footer .btnSave");e.on("hidden.bs.modal",(function(){e.off("hidden.bs.modal"),e.remove()})).modal("show"),o.on("click",(function(n){var t=l(n.currentTarget).attr("data-action"),a=e.find(".optList input:enabled[type=checkbox]"),o=e.find(".optList tbody");switch(t){case"select-all":a.prop("checked",!0),(0,c.postRender)(o);break;case"unselect-all":a.prop("checked",!1),(0,c.postRender)(o)}})),i.on("click",(function(){var t=l("#wizardSetDataframeIndex .optList input[type=checkbox]:checked"),o=a.options.confirm.params.columns;t.each((function(n,t){o.push(l(t).val())})),(new n).callWizard(a.options.confirm,(function(){e.modal("hide"),a.options.callback()}))})),this.getData()},getData:function(){var t=l("#wizardSetDataframeIndex .optList"),e=l("#wizardSetDataframeIndex .optList tbody");(new n).callWizard(this.options.bodyParams,(function(n){n.forEach((function(n){var t=n.field,l=n.type,o=n.dtype;e.append(a({field:t,dtype:o,checked:l===d.TYPES.INDEX}))})),(0,c.postRender)(e),t.show()}))}})}.apply(t,o))||(n.exports=i)}).call(this,a(219),a(1))},1265:function(n,t,a){var e=a(670);function l(n){return n&&(n.__esModule?n.default:n)}n.exports=(e.default||e).template({compiler:[8,">= 4.3.0"],main:function(n,t,e,o,i){var c=n.lambda,d=n.escapeExpression,s=null!=t?t:n.nullContext||{},u=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return"<div id='wizardSetDataframeIndex' class='modal fade nodeWizardDialog' tabindex='-1' role='dialog'\n  aria-labelledby='Wizard' aria-hidden='true'>\n  <div class='modal-dialog'>\n    <div class='modal-content'>\n      <div class='modal-header'>\n        <button type='button' class='close' data-dismiss='modal' aria-hidden='true'>x</button>\n        <h4>"+d(c(null!=t?u(t,"title"):t,t))+"</h4>\n      </div>\n      <div class='modal-body nopadding' style=\"max-height:"+d(c(null!=t?u(t,"max_height"):t,t))+"\">\n        <div class='nodisplay optList'>\n          <table class='table table-nomargin'>\n            <thead>\n              <tr>\n                <th>"+d(l(a(668)).call(s,"include",{name:"L",hash:{},data:i,loc:{start:{line:14,column:20},end:{line:14,column:35}}}))+"</th>\n                <th>"+d(l(a(668)).call(s,"variable",{name:"L",hash:{},data:i,loc:{start:{line:15,column:20},end:{line:15,column:36}}}))+"</th>\n                <th>"+d(l(a(668)).call(s,"_dtype",{name:"L",hash:{},data:i,loc:{start:{line:16,column:20},end:{line:16,column:34}}}))+"</th>\n              </tr>\n            </thead>\n            <tbody>\n            </tbody>\n          </table>\n        </div>\n      </div>\n      <div class='commandButtons'>\n        <button type='button' class='btn btn-green' rel='tooltip' data-original-title=\""+d(l(a(668)).call(s,"_select_all",{name:"L",hash:{},data:i,loc:{start:{line:25,column:87},end:{line:25,column:106}}}))+"\"\n          data-action='select-all'>\n          <i class='fa fa-check' /> "+d(l(a(668)).call(s,"_select_all",{name:"L",hash:{},data:i,loc:{start:{line:27,column:36},end:{line:27,column:55}}}))+"\n        </button>\n        <button type='button' class='btn btn-orange' rel='tooltip' data-original-title=\""+d(l(a(668)).call(s,"_unselect_all",{name:"L",hash:{},data:i,loc:{start:{line:29,column:88},end:{line:29,column:109}}}))+"\"\n          data-action='unselect-all'>\n          <i class='fa fa-close' /> "+d(l(a(668)).call(s,"_unselect_all",{name:"L",hash:{},data:i,loc:{start:{line:31,column:36},end:{line:31,column:57}}}))+"\n        </button>\n      </div>\n      <div class='modal-footer'>\n        <button type='button' class='btn btn-default' data-dismiss='modal'>"+d(l(a(668)).call(s,"cancel",{name:"L",hash:{},data:i,loc:{start:{line:35,column:75},end:{line:35,column:89}}}))+"</button>\n        <button type='button' class='btn btn-primary btnSave'>"+d(l(a(668)).call(s,"_set_index",{name:"L",hash:{},data:i,loc:{start:{line:36,column:62},end:{line:36,column:80}}}))+"</button>\n      </div>\n    </div>\n  </div>\n</div>"},useData:!0})},1266:function(n,t,a){var e=a(670);n.exports=(e.default||e).template({1:function(n,t,a,e,l){return" checked "},compiler:[8,">= 4.3.0"],main:function(n,t,a,e,l){var o,i,c=null!=t?t:n.nullContext||{},d=n.hooks.helperMissing,s=n.escapeExpression,u=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return"<tr>\n  <td>\n    <input type='checkbox' class='icheck-me' data-skin='square' data-color='blue' "+(null!=(o=u(a,"if").call(c,null!=t?u(t,"checked"):t,{name:"if",hash:{},fn:n.program(1,l,0),inverse:n.noop,data:l,loc:{start:{line:3,column:82},end:{line:3,column:113}}}))?o:"")+"\n      value='"+s("function"==typeof(i=null!=(i=u(a,"field")||(null!=t?u(t,"field"):t))?i:d)?i.call(c,{name:"field",hash:{},data:l,loc:{start:{line:4,column:13},end:{line:4,column:22}}}):i)+"' data-type='"+s("function"==typeof(i=null!=(i=u(a,"dtype")||(null!=t?u(t,"dtype"):t))?i:d)?i.call(c,{name:"dtype",hash:{},data:l,loc:{start:{line:4,column:35},end:{line:4,column:44}}}):i)+"' />\n  </td>\n  <td>\n    <span>"+s("function"==typeof(i=null!=(i=u(a,"field")||(null!=t?u(t,"field"):t))?i:d)?i.call(c,{name:"field",hash:{},data:l,loc:{start:{line:7,column:10},end:{line:7,column:19}}}):i)+"</span>\n  </td>\n  <td>"+s("function"==typeof(i=null!=(i=u(a,"dtype")||(null!=t?u(t,"dtype"):t))?i:d)?i.call(c,{name:"dtype",hash:{},data:l,loc:{start:{line:9,column:6},end:{line:9,column:15}}}):i)+"</td>\n</tr>"},useData:!0})},732:function(n,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.TYPES=t.DTYPES=void 0;t.DTYPES={STRING:"string",NUMERIC:"numeric",BOOLEAN:"boolean",DATE:"date",OBJECT:"object",VOID:"void"};t.TYPES={INDEX:"index",COLUMN:"column"}}}]);