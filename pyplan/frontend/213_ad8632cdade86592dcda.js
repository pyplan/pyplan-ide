/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[213],{1842:function(n,e,a){var o=a(690);function l(n){return n&&(n.__esModule?n.default:n)}n.exports=(o.default||o).template({1:function(n,e,o,t,d){var i,s=null!=e?e:n.nullContext||{};return"                <dt>"+n.escapeExpression(l(a(688)).call(s,null!=e?e.Key:e,{name:"L",hash:{},data:d}))+":</dt>\n                <dd>"+(null!=(i=o.if.call(s,null!=e?e.Value:e,{name:"if",hash:{},fn:n.program(2,d,0),inverse:n.program(4,d,0),data:d}))?i:"")+"</dd>\n"},2:function(n,e,a,o,l){return n.escapeExpression(n.lambda(null!=e?e.Value:e,e))},4:function(n,e,a,o,l){return" - "},compiler:[7,">= 4.0.0"],main:function(n,e,o,t,d){var i,s=null!=e?e:n.nullContext||{},c=n.escapeExpression;return'<div id="modelInfoModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n        <h3>'+c(l(a(688)).call(s,"model_info",{name:"L",hash:{},data:d}))+'</h3>\n      </div>\n      <div class="modal-body">\n        <dl>\n'+(null!=(i=o.each.call(s,e,{name:"each",hash:{},fn:n.program(1,d,0),inverse:n.noop,data:d}))?i:"")+'        </dl>\n\n        <div class="row">\n          <div class="col-md-12">\n            <button class="btn btn-lightred closeModel">'+c(l(a(688)).call(s,"close_model",{name:"L",hash:{},data:d}))+"</button>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n</div>\n"},useData:!0})},995:function(n,e,a){"use strict";(function(o,l,t){var d,i,s=a(18);d=[a(684),a(219),a(1842)],void 0===(i=function(n,e,d){return o.View.extend({el:l("#main"),nodeDic:{},render:function(o){var i=this,c=new e;c.getModelInfo(function(e){var o=d(e);i.$el.append(o),l("#modelInfoModal").on("hidden.bs.modal",function(){l("#modelInfoModal").off("hidden"),l("#modelInfoModal").remove()}).modal("show"),l("#modelInfoModal .closeModel").on("click",function(e){var o=!1;l("a.btnSaveModel").length>0&&l("a.btnSaveModel").is(":visible")&&(o=l("a.btnSaveModel").parent().hasClass("modelopened with-pending-changes"));var d=l("#main .mainTask").length,i=function e(){var a=0;l("#main .mainTask").each(function(o,d){var i=t.Event("beforeRemoveView");if(l(this).trigger(i,[function(){a++,e()}]),i.isDefaultPrevented())return(new n).selectTask(l(this).attr("data-rel")),!1;a++}),a>=d&&r()},r=function(){c.closeModel(function(){l("#summary").trigger("refresh"),l("#modelInfoModal").modal("hide")})};o?(l("#modelInfoModal").modal("hide"),Promise.resolve().then(function(){var n=[a(683)];(function(n){(new n).show({title:(0,s.translate)("model_changes_title"),text:(0,s.translate)("model_changes_text_close"),buttons:[{title:(0,s.translate)("model_changes_confirm"),css:"primary",code:"yes"},{title:(0,s.translate)("model_changes_discard_close"),code:"no"}],callback:function(n){"yes"==n?Promise.resolve().then(function(){var n=[a(219)];(function(n){(new n).saveModel(function(){setTimeout(function(){i()},1e3)})}).apply(null,n)}).catch(a.oe):setTimeout(function(){i()},1e3)}})}).apply(null,n)}).catch(a.oe)):i()})})}})}.apply(e,d))||(n.exports=i)}).call(this,a(218),a(1),a(1))}}]);