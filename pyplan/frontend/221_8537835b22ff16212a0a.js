/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[221,5],{1925:function(n,e,a){"use strict";(function(t,i){var l,o,s=a(18);l=[a(683),a(1926)],void 0===(o=function(n,e){new n;return t.View.extend({el:i("#main"),render:function(a){var t=this,i=(0,s.translate)("_sendTestEmail");!function(){var l=e();(new n).show({title:i,html:l,modalClass:"sendTestEmailModal",buttons:[{title:(0,s.translate)("_send"),code:"send",css:"primary"},{title:(0,s.translate)("cancel"),code:"close"}],callback:function(n,e){if("send"==n){if(!(0,s.cubeValidate)(e.find("#formSendTestEmail")))return!1;var i=e.find("input[name='email']").val();a(t.options,i),e.modal("hide")}},onLoad:function(n){setTimeout(function(){},500),(0,s.postRender)(n)},onClose:function(n){t.destroy(n)}})}(),t.addHandlers()},addHandlers:function(){},destroy:function(){}})}.apply(e,l))||(n.exports=o)}).call(this,a(218),a(1))},1926:function(n,e,a){var t=a(690);function i(n){return n&&(n.__esModule?n.default:n)}n.exports=(t.default||t).template({compiler:[7,">= 4.0.0"],main:function(n,e,t,l,o){var s=null!=e?e:n.nullContext||{},r=n.escapeExpression;return'\x3c!-- container starts --\x3e\n<div class="container-fluid">\n    \x3c!-- first row --\x3e\n    <div class="row">\n        <form action="#" method="POST" class=\'form-validate\' id="formSendTestEmail">\n            \n           \x3c!-- first subrow --\x3e\n            <div class="row">\n                <div class="col-sm-12">\n                    <div class="form-group">\n                        <label class="control-label">'+r(i(a(688)).call(s,"_email",{name:"L",hash:{},data:o}))+'</label>\n                        <span class="tooltip-warning" rel="tooltip" data-title="'+r(i(a(688)).call(s,"_enterEmail",{name:"L",hash:{},data:o}))+'" data-placement="right"><i class="fa fa-info-circle fa-primary"></i></span>\n                        <input type="email" name="email" class="form-control" data-rule-required="true" data-rule-email="true" />\n                    </div>\n                </div>\n            </div>                      \n        </form>\n    </div>\t\n\n\x3c!-- container ends --\x3e\n</div>'},useData:!0})},683:function(n,e,a){"use strict";(function(t){var i;void 0===(i=function(){return t.Controller.extend({name:"showModal",show:function(n){Promise.all([a.e(2),a.e(118)]).then(function(){var e=[a(700)];(function(e){(new e).render(n)}).apply(null,e)}).catch(a.oe)}})}.apply(e,[]))||(n.exports=i)}).call(this,a(694))}}]);