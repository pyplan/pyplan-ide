/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[234],{1969:function(l,n,a){"use strict";(function(t,o){var s,i;s=[a(219),a(1970)],void 0===(i=function(l,n){return t.View.extend({el:o("#main"),fromLine:"1",render:function(a){if(!(this.$el.find(".installLibsModal").length>0)){var t=this,s=n(a);this.$el.append(s),o(".pipInstallConsole").perfectScrollbar(),o(".installLibsModal .btnStartInstall").on("click",function(){t.fromLine=0,o(".pipInstallConsole").html("");var n=new l,a=o(".installLibsModal").find(".libToInstall").val();n.installLibrary(a,function(l){!function l(){o(".installLibsModal").length>0&&o(".pipInstallConsole").length>0&&setTimeout(function(){n.getInstallProgress(t.fromLine,function(n){n.length>0&&(n.forEach(function(l){o(".pipInstallConsole").append('<pre class="reset">'+l+"</pre>"),o(".pipInstallConsole").scrollTop(o(".pipInstallConsole").prop("scrollHeight")),o(".pipInstallConsole").perfectScrollbar("update")}),t.fromLine=(parseInt(t.fromLine)+n.length).toString()),l()},function(n){t.fromLine,clearTimeout(l)})},2e3)}()})}),o(".installLibsModal .modal-footer button").click(function(){var l=!0;return a.callback&&!1===a.callback.call(this,o(this).attr("data-code"),o(".installLibsModal"))&&(l=!1),l&&(o(".installLibsModal").off("shown"),o(".installLibsModal").modal("hide")),!1}),o(".installLibsModal").on("show.bs.modal",function(){if(0===o(".installLibsModal:visible").length){var l=100014+10*o(".modal:visible").length;o(this).css("z-index",l),setTimeout(function(){o(".modal-backdrop").not(".modal-stack").css("z-index",l-10).addClass("modal-stack")},0),a.hasOwnProperty("onLoad")&&a.onLoad(o(".installLibsModal")),!0!==a.okOnEnter&&void 0!==a.okOnEnter||o(".installLibsModal").keyup(function(l){13==l.keyCode&&o(".installLibsModal button.btn-primary").click()})}}),o(".installLibsModal").on("hidden.bs.modal",function(){o(".installLibsModal").off("hidden"),a.hasOwnProperty("onClose")&&a.onClose(o(".installLibsModal")),o(".manageLibsModal").trigger("refreshData"),o(".installLibsModal").remove()});var i=null;a.backdrop&&(i={backdrop:"static",keyboard:!1}),o(".installLibsModal").modal(i)}}})}.apply(n,s))||(l.exports=i)}).call(this,a(218),a(1))},1970:function(l,n,a){var t=a(690);l.exports=(t.default||t).template({1:function(l,n,a,t,o){var s,i=null!=n?n:l.nullContext||{},e=a.helperMissing,d=l.escapeExpression;return'        <button class="btn btn-'+d("function"==typeof(s=null!=(s=a.css||(null!=n?n.css:n))?s:e)?s.call(i,{name:"css",hash:{},data:o}):s)+'" data-code="'+d("function"==typeof(s=null!=(s=a.code||(null!=n?n.code:n))?s:e)?s.call(i,{name:"code",hash:{},data:o}):s)+'" data-dismiss="modal" aria-hidden="true">'+d("function"==typeof(s=null!=(s=a.title||(null!=n?n.title:n))?s:e)?s.call(i,{name:"title",hash:{},data:o}):s)+"</button>\n"},compiler:[7,">= 4.0.0"],main:function(l,n,a,t,o){var s,i,e=null!=n?n:l.nullContext||{},d=a.helperMissing,c=l.escapeExpression;return'<div id="main-modal" class="modal fade installLibsModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"\n  aria-hidden="true" data-backdrop="static" data-keyboard="false" style="display: none;">\n  <div class="modal-dialog '+c("function"==typeof(i=null!=(i=a.modalClass||(null!=n?n.modalClass:n))?i:d)?i.call(e,{name:"modalClass",hash:{},data:o}):i)+'">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n        <h4 class="modal-title" id="myModalLabel">'+c("function"==typeof(i=null!=(i=a.title||(null!=n?n.title:n))?i:d)?i.call(e,{name:"title",hash:{},data:o}):i)+'</h4>\n      </div>\n\n      <div class="modal-body" style="overflow-y:auto; overflow-x: hidden;">\n\n        <div class="row form-horizontal">\n          <div class="col-sm-12">\n\n\n            <div class="form-group">\n              <label for="textfield" class="control-label col-sm-3" style="font-family: monospace;">pip\n                install</label>\n              <div class="col-sm-9">\n                <div class="input-group">\n                  <input class="form-control libToInstall col-sm-12" type="text" name="textfield" id="textfield"\n                    value="">\n                  <div class="input-group-btn">\n                    <button class="btn btn-primary btnStartInstall" type="button"> <i class="fas fa-play"></i> </button>\n                  </div>\n                </div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="row">\n          <div class="col-sm-12">\n            <div class="pipInstallConsole">\n\n            </div>\n          </div>\n        </div>\n\n      </div>\n      <div class="modal-footer">\n'+(null!=(s=a.each.call(e,null!=n?n.buttons:n,{name:"each",hash:{},fn:l.program(1,o,0),inverse:l.noop,data:o}))?s:"")+"      </div>\n    </div>\n  </div>\n</div>"},useData:!0})}}]);