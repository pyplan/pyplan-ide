/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[232],{1952:function(e,a,n){"use strict";(function(o,t){var s,i,l=n(18);n(1953),n(1954),n(1955),n(1956),n(1957),n(1958),n(1959),s=[n(219),n(1960),n(1961)],void 0===(i=function(e,a,s){return o.View.extend({el:t("#main"),diagram:void 0,colorpickerInstanced:!1,render:function(){var o=this;(new e).getToolbars(function(e){var s={hasOptimizer:!1,toolbars:e};__currentSession&&__currentSession.modelInfo&&__currentSession.modelInfo.edition&&__currentSession.modelInfo.edition.toLowerCase().indexOf("ade optimizer")>=0&&(s.hasOptimizer=!0);var i=a(s);o.$el.append(i);for(var r=10;r<60;r++)t("<option/>").val(r).text(r).appendTo(o.$el.find('select[name="fontSize"]'));if((0,l.postRender)(o.getBase()),o.listShortcuts(),o.addHandlers(),(0,l.haveAccess)("change_influence_diagram")){"false"===t.cookie("cubeplan_edit_mode")&&!1}o.instanceColorPicker(null);var d=new plupload.Uploader({runtimes:"html5",browse_button:"addNodeImage",url:"".concat(__apiURL,"/modelManager/uploadFileToTemp/"),headers:{Authorization:"Token ".concat(__currentToken),"session-key":__currentSession.session_key},file_data_name:"files",multi_selection:!1,max_file_size:"0",chunk_size:"10mb",unique_names:!1,filters:[{title:"Image files",extensions:"jpg,gif,png"}],flash_swf_url:"js/plupload/plupload.flash.swf",silverlight_xap_url:"js/plupload/plupload.silverlight.xap",multipart_params:{action:"uploadFileToTemp"},init:{PostInit:function(){},FilesAdded:function(e,a){plupload.each(a,function(e){o.getBase().find(".sr-only").html("Uploading file..."),o.getBase().find(".import-progressbar").toggle(),o.getBase().find(".btn-upload").toggle(),d.start()})},UploadProgress:function(e,a){o.getBase().find(".progress-bar").css("width",a.percent+"%")},UploadComplete:function(e,a){},FileUploaded:function(e,a,s){if(s&&""!=s.response&&"ok"!=s.response){var i=o.options.diagram.getSelectedNodes()[0].id,l=s.response.slice(1,-1);Promise.resolve().then(function(){var e=[n(219)];(function(e){(new e).setNodeProperties(i,[{name:"picture",value:l}],function(e){t(".mainTask.influence-diagram").trigger("refreshView"),o.getBase().find(".nodeImage #addNodeImage").hide(),o.getBase().find(".nodeImage .moxie-shim.moxie-shim-html5").hide(),o.getBase().find(".nodeImage #removeNodeImage").show()})}).apply(null,e)}).catch(n.oe)}},Error:function(e,a){document.getElementById("console").innerHTML+="\nError #"+a.code+": "+a.message}}});d.init()})},onRemoveView:function(){this.getBase().find(".ui-colorpicker").length>0&&this.getBase().find(".node-color").colorpicker("destroy"),(0,l.removeResizeEvent)("toolbarDiagramResize")},updateSizes:function(){},getBase:function(){return this.$el.find(".diagram-toolbar")},instanceColorPicker:function(e){var a=this;this.getBase().find(".node-color").colorpicker({parts:["preview","map","bar","hex","rgb","memory","swatches","swatchesswitcher"],alpha:!1,layout:{map:[0,0,3,4],bar:[3,0,1,4],preview:[4,0,1,1],hex:[4,1,1,1],rgb:[4,2,1,1],memory:[4,3,1,1],swatchesswitcher:[5,0,1,1],swatches:[5,1,1,3]},select:function(e,n){for(var o=a.options.diagram.getSelectedNodes(),t=[],s=0;s<o.length;s++)t.push(o[s].id);!0===a.colorpickerInstanced?t.length>0&&a.options.diagram.setNodeColor(t,n.css):a.colorpickerInstanced=!0}}),this.getBase().find(".node-color").colorpicker("setColor",e),a.colorpickerInstanced=!0},listShortcuts:function(){Promise.resolve().then(function(){var e=[n(219)];(function(e){(new e).listShortcuts(function(e){var a=s({shortcut:e});t("li.shortcuts ul").append(a)})}).apply(null,e)}).catch(n.oe)},installLibs:function(){Promise.resolve().then(function(){var e=[n(714)];(function(e){(new e).installLibsModal({title:(0,l.translate)("install_libraries"),okOnEnter:!1,modalClass:"mediumModal",buttons:[{title:(0,l.translate)("close"),code:"cancel"}],onLoad:function(e){e.find(".pureHtmlEditor").focus()}})}).apply(null,e)}).catch(n.oe)},manageLibs:function(){Promise.resolve().then(function(){var e=[n(714)];(function(e){(new e).manageLibsModal({title:(0,l.translate)("manage_libraries"),okOnEnter:!1,modalClass:"mediumModal"})}).apply(null,e)}).catch(n.oe)},addHandlers:function(){var e=this,a=t(".mainTask.influence-diagram");a.on("diagramClick",function(){e.getBase().find(".make_alias").hide(),e.getBase().find(".make_same_size").hide(),e.getBase().find(".node_align").hide(),e.getBase().find(".node_z").hide(),e.getBase().find(".shortcuts").show(),e.getBase().find(".appearence").hide(),e.getBase().find(".nodeColor").hide(),e.getBase().find(".nodeImage").hide(),e.getBase().hasClass("browser-mode")||(e.getBase().find(".diagramImport").show(),e.getBase().find(".modelPreferences").show())}),a.on("clearSelect",function(){e.getBase().find(".make_alias").hide(),e.getBase().find(".make_same_size").hide(),e.getBase().find(".node_align").hide()}),a.on("nodeSelect",function(a,n,o){var s=n.nodeInfo;o?(e.getBase().find(".make_alias").show(),e.getBase().find(".node_z").show(),e.getBase().find(".appearence").show(),e.getBase().find(".nodeColor").show(),e.getBase().find(".nodeImage").show(),e.getBase().find(".make_same_size").hide(),e.getBase().find(".node_align").hide(),e.getBase().find(".shortcuts").hide()):(e.getBase().find(".make_alias").hide(),e.getBase().find(".node_z").hide(),e.getBase().find(".appearence").hide(),e.getBase().find(".nodeColor").hide(),e.getBase().find(".nodeImage").hide(),e.getBase().find(".make_same_size").hide(),e.getBase().find(".node_align").hide(),e.getBase().find(".shortcuts").show()),n.hasPicture?(e.getBase().find(".nodeImage #addNodeImage").hide(),e.getBase().find(".nodeImage .moxie-shim.moxie-shim-html5").hide(),e.getBase().find(".nodeImage #removeNodeImage").show()):(e.getBase().find(".nodeImage #addNodeImage").show(),e.getBase().find(".nodeImage .moxie-shim.moxie-shim-html5").show(),e.getBase().find(".nodeImage #removeNodeImage").hide()),e.getBase().find(".diagramImport").hide(),e.getBase().find(".modelPreferences").hide();var i,l,r=n.nodeClass;n.originalClass&&(r=n.originalClass),"text"==r||"button"==r||"function"==r||"module"==r||"linkmodule"==r?e.getBase().find(".make_alias .node-action.io").hide():e.getBase().find(".make_alias .node-action.io").show(),n.color&&(e.colorpickerInstanced=!1,e.getBase().find(".node-color").colorpicker("setColor",n.color.toString())),t('ul li.node-style input[type="checkbox"]').each(function(a,o){if(i=t(o).attr("rel"),l=!0,"1"!==s[i]&&(l=!1),t(o).prop("checked",l),"useNodeFont"===i)if(!0===l){e.getBase().find(".fontSize").prop("disabled",!1),e.getBase().find(".fontName").prop("disabled",!1),e.getBase().find(".fontSelector").show();var r=n.nodeFont.split(",");e.getBase().find(".fontName").val(r[0]),e.getBase().find(".fontSize").val(96/72*parseFloat(r[1]))}else e.getBase().find(".fontSelector").hide(),e.getBase().find(".fontSize").prop("disabled",!0),e.getBase().find(".fontName").prop("disabled",!0)})}),a.on("nodesSelect",function(a,n,o){o?(e.getBase().find(".make_alias").show(),e.getBase().find(".make_same_size").show(),e.getBase().find(".node_align").show(),e.getBase().find(".appearence").show(),e.getBase().find(".nodeColor").show(),e.getBase().find(".node_z").show(),e.getBase().find(".nodeImage").hide(),e.getBase().find(".diagramImport").hide(),e.getBase().find(".modelPreferences").hide()):(e.getBase().find(".make_alias").hide(),e.getBase().find(".make_same_size").hide(),e.getBase().find(".node_align").hide(),e.getBase().find(".appearence").hide(),e.getBase().find(".nodeColor").hide(),e.getBase().find(".node_z").hide(),e.getBase().find(".nodeImage").hide(),e.getBase().find(".diagramImport").hide(),e.getBase().find(".modelPreferences").hide());for(var s,i,l=n[n.length-1].nodeInfo,r=n[n.length-1].color,d=0;d<n.length;d++){var c=n[d].nodeClass,f=!0;n[d].originalClass&&(c=n[d].originalClass),"text"!=c&&"button"!=c&&"function"!=c&&"module"!=c&&"library"!=c||(f=!1),1==f?e.getBase().find(".make_alias .node-action.io").show():e.getBase().find(".make_alias .node-action.io").hide()}r&&(e.colorpickerInstanced=!1,e.getBase().find(".node-color").colorpicker("setColor",r)),t('ul li.node-style input[type="checkbox"]').each(function(e,a){s=t(a).attr("rel"),i=!0,"1"!==l[s]&&(i=!1),t(a).prop("checked",i)})}),this.getBase().find("ul li.diagram-node").on("mousedown",function(e){a.find(".diagram-toolbar ul li ul").hide();var n=t(this).find("a").attr("rel-wizard");t(document).one("mouseup",function(){a.find(".diagram-toolbar ul li ul").show()});var o=t(this).find("a").attr("rel"),s=t(this).find("a").attr("rel-base");t(".diagram-toolbar").css("opacity","0.2"),a.find(".diagram-area").trigger("startCreateNewNode",[o,s,n]),e.preventDefault(),e.stopPropagation()}),this.getBase().find(".btnEditSelector a").on("click",function(){var a=!1;e.getBase().hasClass("browser-mode")?(a=!0,e.getBase().removeClass("browser-mode"),t(this).html('<i class="fa fa-mouse-pointer"></i> '+(0,l.translate)("toggle_browse_mode")),e.getBase().css("height","100%")):(a=!1,e.getBase().addClass("browser-mode"),t(this).html('<i class="fa fa-pencil-square-o"></i> '+(0,l.translate)("toggle_edit_mode")),e.getBase().css("height","35px")),e.getBase().closest(".influence-diagram").trigger("changeEditMode",[a]),!1===a?(e.getBase().find(".appearence").hide(),e.getBase().find(".nodeColor").hide(),e.getBase().find(".nodeImage").hide(),e.getBase().find(".diagramImport").hide(),e.getBase().find(".modelPreferences").hide(),e.getBase().find(".node_z").hide()):(e.getBase().find(".diagramImport").show(),e.getBase().find(".modelPreferences").show())}),this.getBase().find(".diagramImport a").on("click",function(e){Promise.resolve().then(function(){var e=[n(714)];(function(e){(new e).importModuleModal("",function(e){})}).apply(null,e)}).catch(n.oe)}),this.getBase().find(".modelPreferences a").on("click",function(e){var a={title:(0,l.translate)("_model_preferences"),buttons:[{code:"save",title:"Save",css:"primary"},{code:"cancel",title:"Cancel",css:"red"}]};Promise.resolve().then(function(){var e=[n(714)];(function(e){(new e).showModelPreferencesModal(a,function(e){})}).apply(null,e)}).catch(n.oe)}),this.getBase().find(".btnManageLibraries a").on("click",function(a){e.manageLibs()}),this.getBase().find(".node-action a").on("click",function(a){switch(t(this).attr("rel")){case"alias":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("createAlias");break;case"inputnode":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("createInputNode");break;case"outputnode":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("createOutputNode");break;case"duplicate":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("duplicateNodes");break;case"same_width":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("makeSameSize",[1]);break;case"same_height":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("makeSameSize",[2]);break;case"same_both":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("makeSameSize");break;case"align_node":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("alignNodes",[parseInt(t(this).attr("data-key"))]);break;case"sendToBack":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("sendToBack");break;case"bringToFront":e.getBase().closest(".influence-diagram").find(".diagram-area").trigger("bringToFront")}}),this.getBase().on("click",'a[rel="addShortcut"]',function(a){var o=t(".model-breadcrumb span").attr("data-module-id");Promise.resolve().then(function(){var a=[n(219)];(function(a){(new a).createShortcut(o,function(a){(0,l.showMessage)((0,l.translate)("shortcut_created"),(0,l.translate)("success"),"success"),t("li.shortcuts ul").empty(),e.listShortcuts()})}).apply(null,a)}).catch(n.oe)}),this.getBase().on("click",'a[rel="navigateTo"]',function(a){if(!1===t(a.target).hasClass("removeShortcut")){var n=t(this).attr("node-id");e.options.diagram.navigateThisModule(n)}}),this.getBase().on("click","i.removeShortcut",function(a){a.preventDefault();var o=t(this).closest("a").attr("shortcut-id");Promise.resolve().then(function(){var a=[n(219)];(function(a){(new a).deleteShortcut(o,function(a){(0,l.showMessage)((0,l.translate)("shortcut_deleted"),(0,l.translate)("success"),"info"),t("li.shortcuts ul").empty(),e.listShortcuts()})}).apply(null,a)}).catch(n.oe)}),this.getBase().find('select[name="fontSize"], select[name="fontName"]').on("change",function(a){for(var n=e.options.diagram.getSelectedNodes(),o=[],t=0;t<n.length;t++)o.push(n[t].id);var s=.75*parseInt(e.getBase().find(".fontSize").val()),i=e.getBase().find(".fontName").val()+","+s;e.options.diagram.setNodeFont(o,i)}),this.getBase().find('.node-style input[type="checkbox"]').on("change",function(a){for(var n=e.options.diagram.getSelectedNodes(),o=[],s=0;s<n.length;s++)o.push(n[s].id);var i,l,r=new Object;t('ul li.node-style input[type="checkbox"]').each(function(a,n){if(i=t(n).attr("rel"),l=n.checked?"1":"0",r[i]=l,"useNodeFont"===i)if("1"===l){e.getBase().find(".fontSize").prop("disabled",!1),e.getBase().find(".fontName").prop("disabled",!1),e.getBase().find(".fontSelector").show();var s=.75*parseInt(e.getBase().find(".fontSize").val()),d=e.getBase().find(".fontName").val()+","+s;e.options.diagram.setNodeFont(o,d)}else e.getBase().find(".fontSize").prop("disabled",!0),e.getBase().find(".fontName").prop("disabled",!0),e.getBase().find(".fontSelector").hide(),e.options.diagram.setNodeFont(o,"")}),o.length>0&&e.options.diagram.setNodeStyle(o,r)}),this.getBase().find(".node-color input").on("change",function(a){for(var n=e.options.diagram.getSelectedNodes(),o=[],t=0;t<n.length;t++)o.push(n[t].id);var s=a.currentTarget.value;o.length>0&&e.options.diagram.setNodeColor(o,s)}),this.getBase().find(".node-color a").on("click",function(e){return e.preventDefault(),!1}),this.getBase().find("li.nodeColor a").on("click",function(e){return e.preventDefault(),!1}),this.getBase().find(".nodeImage #removeNodeImage").on("click",function(){var a=e.options.diagram.getSelectedNodes()[0].id;Promise.resolve().then(function(){var o=[n(219)];(function(n){(new n).setNodeProperties(a,[{name:"picture",value:""}],function(a){t(".mainTask.influence-diagram").trigger("refreshView"),e.getBase().find(".nodeImage #addNodeImage").show(),e.getBase().find(".nodeImage .moxie-shim.moxie-shim-html5").show(),e.getBase().find(".nodeImage #removeNodeImage").hide()})}).apply(null,o)}).catch(n.oe)})}})}.apply(a,s))||(e.exports=i)}).call(this,n(218),n(1))},1960:function(e,a,n){var o=n(690);function t(e){return e&&(e.__esModule?e.default:e)}e.exports=(o.default||o).template({1:function(e,a,o,s,i){var l,r=e.lambda,d=e.escapeExpression,c=null!=a?a:e.nullContext||{};return'    <div class="panel panel-default blue">\n      <div class="panel-heading">\n        <h4 class="panel-title">\n          <a href="#tab-'+d(r(i&&i.index,a))+'" data-toggle="collapse" data-parent="#ac5"\n            class=\''+(null!=(l=t(n(689)).call(c,i&&i.index,">",0,{name:"ifCond",hash:{},fn:e.program(2,i,0),inverse:e.noop,data:i}))?l:"")+"'>\n            "+d(r(null!=a?a.label:a,a))+'\n          </a>\n        </h4>\n        \x3c!-- /.panel-title --\x3e\n      </div>\n      \x3c!-- /.panel-heading --\x3e\n      <div id="tab-'+d(r(i&&i.index,a))+"\" class='panel-collapse collapse "+(null!=(l=t(n(689)).call(c,i&&i.index,"==",0,{name:"ifCond",hash:{},fn:e.program(4,i,0),inverse:e.noop,data:i}))?l:"")+"'\n        style='"+(null!=(l=t(n(689)).call(c,i&&i.index,">",0,{name:"ifCond",hash:{},fn:e.program(6,i,0),inverse:e.noop,data:i}))?l:"")+'\'>\n        <div class="panel-body">\n          <ul>\n'+(null!=(l=o.each.call(c,null!=a?a.items:a,{name:"each",hash:{},fn:e.program(8,i,0),inverse:e.noop,data:i}))?l:"")+"          </ul>\n        </div>\n        \x3c!-- /.panel-body --\x3e\n      </div>\n      \x3c!-- /#c1.panel-collapse collapse in --\x3e\n    </div>\n"},2:function(e,a,n,o,t){return" collapsed"},4:function(e,a,n,o,t){return" in"},6:function(e,a,n,o,t){return" height: 0px; "},8:function(e,a,n,o,t){var s=e.lambda,i=e.escapeExpression;return'            <li class="diagram-node" node-class="'+i(s(null!=a?a.nodeClass:a,a))+'">\n              <a href="#" rel="'+i(s(null!=a?a.nodeClass:a,a))+'" rel-base="'+i(s(null!=a?a.baseClass:a,a))+'" rel-icon="'+i(s(null!=a?a.icon:a,a))+'" rel-wizard="'+i(s(null!=a?a.wizard:a,a))+'">\n                <img src="'+i(s(null!=a?a.uiUrl:a,a))+"toolbars/img/nodeTypes/"+i(s(null!=a?a.icon:a,a))+'_icon.png" width="20" height="13">\n                <span class="text">'+i(s(null!=a?a.label:a,a))+"</span>\n              </a>\n            </li>\n"},compiler:[7,">= 4.0.0"],main:function(e,a,o,s,i){var l,r=null!=a?a:e.nullContext||{},d=e.escapeExpression;return'<div class="navigation diagram-toolbar nodeclass-item">\n  <ul>\n    <li class="btnEditSelector" style="height: 33px;">\n      <a href="#" rel="nothing">\n        <i class="fa fa-mouse-pointer"></i> '+d(t(n(688)).call(r,"toggle_browse_mode",{name:"L",hash:{},data:i}))+'\n      </a>\n    </li>\n  </ul>\n\n  <div class="panel-group" id="ac5">\n\n'+(null!=(l=o.each.call(r,null!=a?a.toolbars:a,{name:"each",hash:{},fn:e.program(1,i,0),inverse:e.noop,data:i}))?l:"")+'  </div>\n\n  <ul>\n    <li class="more make_alias nodisplay">\n      <a href="#">\n        <i class="fa fa-clone"></i> Diagram\n      </a>\n\n      <ul class="more-clone">\n        <li class="node-action">\n          <a href="#" rel="alias">\n            <span class="text">'+d(t(n(688)).call(r,"make_alias",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+m)</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="inputnode">\n            <span class="text">'+d(t(n(688)).call(r,"make_input_node",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+alt+i)</span>\n          </a>\n        </li>\n        \x3c!--li class="node-action io">\n          <a href="#" rel="outputnode">\n            <span class="text">'+d(t(n(688)).call(r,"make_output_node",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+alt+o)</span>\n          </a>\n        </li--\x3e\n        <li class="node-action">\n          <a href="#" rel="duplicate">\n            <span class="text">'+d(t(n(688)).call(r,"duplicate",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+d)</span>\n          </a>\n        </li>\n      </ul>\n    </li>\n    <li class="more node_z nodisplay">\n      <a href="#">\n        <i class="fa fa-sort-amount-desc"></i> Organize\n      </a>\n      <ul class="more-clone">\n        <li class="node-action">\n          <a href="#" rel="sendToBack">\n            <span class="text">'+d(t(n(688)).call(r,"node_sendtoback",{name:"L",hash:{},data:i}))+'</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="bringToFront">\n            <span class="text">'+d(t(n(688)).call(r,"node_bringtofront",{name:"L",hash:{},data:i}))+'</span>\n          </a>\n        </li>\n      </ul>\n    </li>\n    <li class="more make_same_size nodisplay">\n      <a href="#">\n        <i class="fa fa-expand"></i> Sizes\n      </a>\n\n      <ul class="more-clone">\n        <li class="node-action">\n          <a href="#" rel="same_width">\n            <span class="text">'+d(t(n(688)).call(r,"make_same_width",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+i)</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="same_height">\n            <span class="text">'+d(t(n(688)).call(r,"make_same_height",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+g)</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="same_both">\n            <span class="text">'+d(t(n(688)).call(r,"make_same_both",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+alt+0)</span>\n          </a>\n        </li>\n      </ul>\n    </li>\n    <li class="more node_align nodisplay">\n      <a href="#">\n        <i class="fa fa-align-left"></i> Alignment\n      </a>\n      <ul class="more-clone">\n        <li class="node-action">\n          <a href="#" rel="align_node" data-key="0">\n            <span class="text">'+d(t(n(688)).call(r,"align_left",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+&larr;)</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="align_node" data-key="1">\n            <span class="text">'+d(t(n(688)).call(r,"align_left_center",{name:"L",hash:{},data:i}))+'</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="align_node" data-key="2">\n            <span class="text">'+d(t(n(688)).call(r,"align_right",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+&rarr;)</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="align_node" data-key="3">\n            <span class="text">'+d(t(n(688)).call(r,"align_left_right",{name:"L",hash:{},data:i}))+'</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="align_node" data-key="4">\n            <span class="text">'+d(t(n(688)).call(r,"align_top",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+&uarr;)</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="align_node" data-key="5">\n            <span class="text">'+d(t(n(688)).call(r,"align_up_center",{name:"L",hash:{},data:i}))+'</span>\n          </a>\n        </li>\n        <li class="node-action io">\n          <a href="#" rel="align_node" data-key="6">\n            <span class="text">'+d(t(n(688)).call(r,"align_down",{name:"L",hash:{},data:i}))+'</span>\n            <span class="shortcut">(ctrl+r&darr;)</span>\n          </a>\n        </li>\n      </ul>\n    </li>\n    <li class="more appearence nodisplay">\n      <a href="#">\n        <i class="fa fa-wrench"></i> Styles\n      </a>\n      <ul class="more-clone" style="width: 480px;">\n        <li class="node-style no-hover">\n          <a href="#">\n            <div class="row" style="position:relative;">\n              <div class="col-sm-4">\n                <input id="showInputs" type="checkbox" rel="showInputs" />\n                <label for="showInputs">'+d(t(n(688)).call(r,"show_inputs",{name:"L",hash:{},data:i}))+'</label>\n                <br />\n                <input id="showOutputs" type="checkbox" rel="showOutputs" />\n                <label for="showOutputs">'+d(t(n(688)).call(r,"show_outputs",{name:"L",hash:{},data:i}))+'</label>\n              </div>\n              <div class="col-sm-4">\n                <input id="showLabel" type="checkbox" rel="showLabel" />\n                <label for="showLabel">'+d(t(n(688)).call(r,"show_label",{name:"L",hash:{},data:i}))+'</label>\n                <br />\n                <input id="showBorder" type="checkbox" rel="showBorder" />\n                <label for="showBorder">'+d(t(n(688)).call(r,"show_border",{name:"L",hash:{},data:i}))+'</label>\n              </div>\n              <div class="col-sm-4">\n                <input id="fill" type="checkbox" rel="fill" />\n                <label for="fill">'+d(t(n(688)).call(r,"fill",{name:"L",hash:{},data:i}))+'</label>\n                <br />\n                <input id="useNodeFont" type="checkbox" rel="useNodeFont" />\n                <label for="useNodeFont">'+d(t(n(688)).call(r,"custom_font",{name:"L",hash:{},data:i}))+'</label>\n              </div>\n            </div>\n\n            <div class="row form-vertical fontSelector" style="position: relative;\n            background-color: #f8f8f8;\n            margin-left: 0;\n            margin-right: 0;\n            padding-top: 10px;\n            padding-bottom: 10px;">\n              <div class="col-sm-5 nopadding">\n                <div class="form-group">\n                  <label for="select" class="control-label col-sm-12">Size</label>\n                  <div class="col-sm-9">\n                    <select name="fontSize" class="form-control fontSize" size="5">\n                    </select>\n                  </div>\n                </div>\n              </div>\n              <div class="col-sm-7">\n                <div class="form-group">\n                  <label for="select" class="control-label col-sm-12">Font</label>\n                  <div class="col-sm-12">\n                    <select name="fontName" class="form-control fontName" size="5">\n                      <option value="Arial" style=\'font-family: Arial\'>Arial</option>\n                      <option value="Arial Black" style=\'font-family: "Arial Black";\'>Arial Black</option>\n                      <option value="Helvetica" style=\'font-family: Helvetica;\'>Helvetica</option>\n                      <option value="Comic Sans MS" style=\'font-family: "Comic Sans MS";\'>Comic Sans MS</option>\n                      <option value="Impact" style=\'font-family: Impact;\'>Impact</option>\n                      <option value="Charcoal" style=\'font-family: Charcoal;\'>Charcoal</option>\n                      <option value="Lucida Sans Unicode" style=\'font-family: "Lucida Sans Unicode";\'>Lucida Sans\n                        Unicode</option>\n                      <option value="Tahoma" style=\'font-family: Tahoma;\'>Tahoma</option>\n                      <option value="Geneva" style=\'font-family: Geneva;\'>Geneva</option>\n                      <option value="Trebuchet MS" style=\'font-family: "Trebuchet MS";\'>Trebuchet MS</option>\n                      <option value="Verdana" style=\'font-family: Verdana;\'>Verdana</option>\n                      <option value="Courier New" style=\'font-family: "Courier New";\'>Courier New</option>\n                      <option value="Courier" style=\'font-family: Courier;\'>Courier</option>\n                      <option value="Lucida Console" style=\'font-family: "Lucida Console";\'>Lucida Console</option>\n                      <option value="Monaco" style=\'font-family: Monaco;\'>Monaco</option>\n                      <option value="monospace" style=\'font-family: monospace;\'>monospace</option>\n                    </select>\n                  </div>\n                </div>\n              </div>\n            </div>\n          </a>\n        </li>\n      </ul>\n    </li>\n    <li class="more nodeColor nodisplay">\n      <a href="#">\n        <i class="fa fa-tint"></i> Color\n      </a>\n      <ul class="more-color">\n        <li class="node-color" style="left: 10px; top: 30px;">\n          <input class="selected-node-color" type="text" rel="nodeColor" />\n        </li>\n      </ul>\n    </li>\n    <li class="more diagramImport">\n      <a href="#" rel="import">\n        <i class="fa fa-upload"></i> '+d(t(n(688)).call(r,"_import_module",{name:"L",hash:{},data:i}))+'\n      </a>\n    </li>\n    <li class="more modelPreferences">\n      <a href="#" rel="modelPreferences">\n        <i class="fa fa-object-group"></i>\n        <span> '+d(t(n(688)).call(r,"_model_preferences",{name:"L",hash:{},data:i}))+'</span>\n      </a>\n    </li>\n    <li class="more btnManageLibraries">\n      <a href="#" rel="manageLibraries">\n        <i class="fas fa-book"></i>\n        <span> '+d(t(n(688)).call(r,"_manage_libs",{name:"L",hash:{},data:i}))+' </span>\n      </a>\n    </li>\n    <li class="more nodisplay nodeImage">\n      <a id="addNodeImage" href="#" rel="tooltip" data-original-title=\''+d(t(n(688)).call(r,"_add_image",{name:"L",hash:{},data:i}))+'\' data-placement="left">\n        <i class="fa fa-image"></i> Add image\n      </a>\n      <a id="removeNodeImage" href="#" rel="tooltip" data-original-title=\''+d(t(n(688)).call(r,"_remove_image",{name:"L",hash:{},data:i}))+'\' data-placement="left">\n        <span>\n          <i class="fa fa-image fa-stack-1x"></i>\n          <i class="fa fa-times" style="font-size: 10px; padding-left: 13px; padding-top: 8px;"></i>\n        </span>\n      </a>\n    </li>\n    <li class="more shortcuts">\n      <a href="#">\n        <i class="fa fa-flash"></i> Shortcuts\n      </a>\n      <ul class="more-clone">\n      </ul>\n    </li>\n  </ul>\n</div>'},useData:!0})},1961:function(e,a,n){var o=n(690);e.exports=(o.default||o).template({1:function(e,a,n,o,t){var s=e.lambda,i=e.escapeExpression;return'<li class="node-action">\n  <a href="#" rel="navigateTo" node-id="'+i(s(null!=a?a.node_id:a,a))+'" shortcut-id="'+i(s(null!=a?a.id:a,a))+'">\n    <span class="text">'+i(s(null!=a?a.name:a,a))+' <i class="fa fa-remove removeShortcut"></i> </span>\n  </a>\n</li>\n'},compiler:[7,">= 4.0.0"],main:function(e,a,o,t,s){var i,l=null!=a?a:e.nullContext||{};return'<li class="node-action">\n  <a href="#" rel="addShortcut">\n    <span class="text"><strong>+ '+e.escapeExpression(function(e){return e&&(e.__esModule?e.default:e)}(n(688)).call(l,"create_shortcut",{name:"L",hash:{},data:s}))+"</strong></span>\n  </a>\n</li>\n"+(null!=(i=o.each.call(l,null!=a?a.shortcut:a,{name:"each",hash:{},fn:e.program(1,s,0),inverse:e.noop,data:s}))?i:"")},useData:!0})}}]);