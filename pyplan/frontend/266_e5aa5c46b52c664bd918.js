/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[266],{1044:function(e,n,a){"use strict";(function(t,l){var o,s,i=a(18);o=[a(663),a(220),a(2199)],void 0===(s=function(e,n,o){return t.View.extend({el:l("#main"),render:function(){var t=new n,s=o();(new e).show({title:(0,i.translate)("save_model_as"),html:s,buttons:[{title:(0,i.translate)("cancel"),code:"cancel"},{title:(0,i.translate)("_save"),css:"primary",code:"ok"}],callback:function(e,n){var o=l("#navigation li.modelopened[data-key='btnSaveModelAs'] a"),s=l("#navigation li.modelopened[data-key='btnSaveModelAs'] a i"),r=l("#navigation .user li[data-key='btnSaveModel']"),d=function(e,n,t){l("body").trigger("pendingChanges",[!1]),(0,i.showMessage)((0,i.translate)("model_successfully_saved"),(0,i.translate)("_successfully_saved"),"success",!0),l("#summary").trigger("refresh"),l("#currentModel").html(t),e.modal("hide"),s.removeClass("fa-paste").addClass("fa-save-all"),o.prop("title",(0,i.translate)("save_model_as")),r.show(),__currentSession.modelInfo.uri=n,Promise.resolve().then((function(){var e=[a(682)];(function(e){(new e).setCurrentUri(n)}).apply(null,e)})).catch(a.oe)};if("ok"==e){var c=n.find("input[name='modelName']").val();return c&&""!=c?l("body").find(".mainTask.influence-diagram").length>0?l(".dockInfluenceDiagramProperty").trigger("saveModelChanges",[!0,function(e){e&&t.saveModelAs(c,(function(e){d(n,e.uri,c)}))}]):t.saveModelAs(c,(function(e){d(n,e.uri,c)})):n.find("input[name='modelName']").focus(),!1}},onLoad:function(e){setTimeout((function(){e.find("input[name='modelName']").inputmask("Regex",{regex:"[a-zA-Z0-9 _()áéíóúÁÉÍÓÚñÑÇ]{1,}"}),e.find("input[name='modelName']").val(l("div.user a#currentModel").text()+" (copy)"),e.find("input[name='modelName']").focus()}),600)}})}})}.apply(n,o))||(e.exports=s)}).call(this,a(219),a(1))},2199:function(e,n,a){var t=a(670);e.exports=(t.default||t).template({compiler:[8,">= 4.3.0"],main:function(e,n,t,l,o){return'\n<div class="form-horizontal">\n    <div class="form-group">\n        <label for="textfield" class="control-label col-sm-4">'+e.escapeExpression((s=a(668),s&&(s.__esModule?s.default:s)).call(null!=n?n:e.nullContext||{},"modelinfo_model_name",{name:"L",hash:{},data:o,loc:{start:{line:4,column:62},end:{line:4,column:90}}}))+'</label>\n        <div class="col-sm-8">\n            <input type="text" class="form-control col-sm-10" name="modelName" value="" >\n        </div>\n    </div>\n</div>';var s},useData:!0})}}]);