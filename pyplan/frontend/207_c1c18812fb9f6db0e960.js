/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[207],{1831:function(e,n,a){var t=a(690);e.exports=(t.default||t).template({compiler:[8,">= 4.3.0"],main:function(e,n,t,o,l){return'\n<div class="form-horizontal">\n    <div class="form-group">\n        <label for="textfield" class="control-label col-sm-4">'+e.escapeExpression(function(e){return e&&(e.__esModule?e.default:e)}(a(688)).call(null!=n?n:e.nullContext||{},"modelinfo_model_name",{name:"L",hash:{},data:l,loc:{start:{line:4,column:62},end:{line:4,column:90}}}))+'</label>\n        <div class="col-sm-8">\n            <input type="text" class="form-control col-sm-10" name="modelName" value="" >\n        </div>\n    </div>\n</div>'},useData:!0})},951:function(e,n,a){"use strict";(function(t,o){var l,i,s=a(18);l=[a(683),a(219),a(1831)],void 0===(i=function(e,n,l){return t.View.extend({el:o("#main"),render:function(){var t=new n,i=l();(new e).show({title:(0,s.translate)("save_model_as"),html:i,buttons:[{title:(0,s.translate)("ok"),css:"primary",code:"ok"},{title:(0,s.translate)("cancel"),code:"cancel"}],callback:function(e,n){var l=o("#navigation li.modelopened[data-key='btnSaveModelAs'] a"),i=o("#navigation li.modelopened[data-key='btnSaveModelAs'] a i"),r=o("#navigation .user li[data-key='btnSaveModel']");if("ok"==e){var d=n.find("input[name='modelName']").val();return d&&""!=d?(o("body").find(".mainTask.influence-diagram").length>0&&o(".dockInfluenceDiagramProperty").trigger("saveModelChanges",!0),setTimeout(function(e){t.saveModelAs(d,function(e){!function(e,n,t){o("body").trigger("pendingChanges",[!1]),(0,s.showMessage)((0,s.translate)("model_successfully_saved")," ","success",!0),o("#summary").trigger("refresh"),o("#currentModel").html(t),e.modal("hide"),i.removeClass("fa-paste").addClass("fa-save-all"),l.prop("title",(0,s.translate)("save_model_as")),r.show(),__currentSession.modelInfo.uri=n,Promise.resolve().then(function(){var e=[a(699)];(function(e){(new e).setCurrentUri(n)}).apply(null,e)}).catch(a.oe)}(n,e.uri,d)})},100)):n.find("input[name='modelName']").focus(),!1}},onLoad:function(e){setTimeout(function(){e.find("input[name='modelName']").inputmask("Regex",{regex:"[a-zA-Z0-9 _()áéíóúÁÉÍÓÚñÑÇ]{1,}"}),e.find("input[name='modelName']").val(o("div.user a#currentModel").text()+" (copy)"),e.find("input[name='modelName']").focus()},600)}})}})}.apply(n,l))||(e.exports=i)}).call(this,a(218),a(1))}}]);