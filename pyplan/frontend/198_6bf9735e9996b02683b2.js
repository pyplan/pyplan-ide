/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[198],{1042:function(n,e,t){"use strict";(function(a,o){var l,s,r=t(18);l=[t(854),t(220),t(2189)],void 0===(s=function(n,e,t){return a.View.extend({el:o("#main"),render:function(n){if(!(this.$el.find(".publishToMyPyplanModal").length>0)){this.itemId=n.itemId,this.itemType=n.itemType,n.buttons=[{css:"primary",extraClass:"btnPublishToMyPyplan",title:(0,r.translate)("accept"),code:"publish"},{title:(0,r.translate)("close"),code:"cancel"}];var e=t(n);this.$el.append(e);var a=o(".publishToMyPyplanModal");a.find(".modal-footer button").click((function(e){e.preventDefault();var t=o(e.target).attr("data-code");return!(n.callback&&!1===n.callback.call(e.target,t,a))&&"cancel"==t&&(a.off("shown"),a.modal("hide")),!1})),a.on("show.bs.modal",(function(){if(0===o(".publishToMyPyplanModal:visible").length){var e=100014+10*o(".modal:visible").length;a.css("z-index",e),setTimeout((function(){o(".modal-backdrop").not(".modal-stack").css("z-index",e-10).addClass("modal-stack")}),0),n.hasOwnProperty("onLoad")&&n.onLoad(a),!0!==n.okOnEnter&&void 0!==n.okOnEnter||a.keyup((function(n){13==n.keyCode&&a.find("button.btn-primary").click()}))}})),a.on("hidden.bs.modal",(function(){a.off("hidden"),n.hasOwnProperty("onClose")&&n.onClose(a),a.remove()})),a.modal(n.backdrop?{backdrop:"static",keyboard:!1}:null),this.addHandlers(a)}},addHandlers:function(t){var a=this,l=t.find(".btnPublishToMyPyplan"),s=t.find(".progressPublishToMyPyplan"),i=t.find(".publishToMyPyplanTextContent"),d=t.find(".externalLinkRow"),c=t.find(".publishedItemLinkInput"),u=t.find(".btnCopyToClipboard"),p=t.find(".btnOpenExternalLink");d.hide(),l.on("click",(function(t){t.preventDefault(),l.prop("disabled",!0),s.show();var u=new n,p=__currentSession.modelInfo.uri.substring(0,__currentSession.modelInfo.uri.lastIndexOf("/"));""==p&&(p=__currentSession.modelInfo.uri.substring(0,__currentSession.modelInfo.uri.lastIndexOf("\\")));var f="dashboard"==a.itemType?[a.itemId]:[],m="report"==a.itemType?[a.itemId]:[];o("body").find(".mainTask.influence-diagram").length>0?o(".dockInfluenceDiagramProperty").trigger("saveModelChanges",[!1,function(n){n?u.exportItemsAndPublish(__currentSession.my_username,__currentSession.my_uuid,p,__currentSession.modelInfo.modelId,f,m,(function(n){var e="https://my.pyplan.org/#shared/".concat(n.id);c.val(e),s.hide(),l.prop("disabled",!1),l.hide(),i.hide(),d.show()})):((0,r.showMessage)((0,r.translate)("error_saving_the_model"),(0,r.translate)("saving_error"),"error"),l.prop("disabled",!1))}]):(new e).saveModel((function(){o("body").trigger("pendingChanges",[!1]),(0,r.showMessage)((0,r.translate)("model_successfully_saved"),(0,r.translate)("_successfully_saved"),"success",!0),u.exportItemsAndPublish(__currentSession.my_username,__currentSession.my_uuid,p,__currentSession.modelInfo.modelId,f,m,(function(n){var e="https://my.pyplan.org/#shared/".concat(n.id);c.val(e),s.hide(),l.prop("disabled",!1),l.hide(),i.hide(),d.show()}))}))})),u.on("click",(function(n){var e=document.createElement("textarea");return e.value=c.val(),document.body.appendChild(e),e.select(),document.execCommand("copy"),document.body.removeChild(e),(0,r.showMessage)((0,r.translate)("copied_to_clipboard"),(0,r.translate)("_successfully_copied"),"success"),!1})),p.on("click",(function(n){open(c.val(),"_blank")}))}})}.apply(e,l))||(n.exports=s)}).call(this,t(219),t(1))},2189:function(n,e,t){var a=t(670);function o(n){return n&&(n.__esModule?n.default:n)}n.exports=(a.default||a).template({1:function(n,e,a,l,s){return"                "+n.escapeExpression(o(t(668)).call(null!=e?e:n.nullContext||{},"about_to_publish_interface",{name:"L",hash:{},data:s,loc:{start:{line:15,column:16},end:{line:15,column:50}}}))+"\n"},3:function(n,e,a,l,s){return"                "+n.escapeExpression(o(t(668)).call(null!=e?e:n.nullContext||{},"about_to_publish_application",{name:"L",hash:{},data:s,loc:{start:{line:18,column:16},end:{line:18,column:52}}}))+"\n"},5:function(n,e,t,a,o){var l,s=n.lambda,r=n.escapeExpression,i=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'        <button class="btn btn-'+r(s(null!=e?i(e,"css"):e,e))+" "+r(s(null!=e?i(e,"extraClass"):e,e))+'" data-code="'+r(s(null!=e?i(e,"code"):e,e))+'" data-dismiss="modal"\n          aria-hidden="true">'+(null!=(l=i(t,"if").call(null!=e?e:n.nullContext||{},null!=e?i(e,"icon"):e,{name:"if",hash:{},fn:n.program(6,o,0),inverse:n.noop,data:o,loc:{start:{line:56,column:29},end:{line:56,column:58}}}))?l:"")+" "+r(s(null!=e?i(e,"title"):e,e))+"</button>\n"},6:function(n,e,t,a,o){var l,s=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return null!=(l=n.lambda(null!=e?s(e,"icon"):e,e))?l:""},compiler:[8,">= 4.3.0"],main:function(n,e,a,l,s){var r,i=n.lambda,d=n.escapeExpression,c=null!=e?e:n.nullContext||{},u=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<div id="main-modal" class="modal fade publishToMyPyplanModal" tabindex="-1" role="dialog"\n  aria-labelledby="myModalLabel" aria-hidden="true" data-backdrop="static" data-keyboard="false" style="display: none;">\n  <div class="modal-dialog '+d(i(null!=e?u(e,"modalClass"):e,e))+'">\n    <div class="modal-content">\n      <div class="modal-header">\n        <h4 class="modal-title" id="myModalLabel">'+d(i(null!=e?u(e,"title"):e,e))+'</h4>\n      </div>\n\n      <div class="modal-body" style="overflow-y:auto; overflow-x: hidden;">\n        <div class="container-fluid">\n          <div class="publishToMyPyplanModalContent">\n            <div class="row publishToMyPyplanTextContent">\n              <div class="col-md-12 col-lg-12">\n'+(null!=(r=o(t(669)).call(c,null!=e?u(e,"itemType"):e,"==","dashboard",{name:"ifCond",hash:{},fn:n.program(1,s,0),inverse:n.noop,data:s,loc:{start:{line:14,column:16},end:{line:16,column:27}}}))?r:"")+(null!=(r=o(t(669)).call(c,null!=e?u(e,"itemType"):e,"==","report",{name:"ifCond",hash:{},fn:n.program(3,s,0),inverse:n.noop,data:s,loc:{start:{line:17,column:16},end:{line:19,column:27}}}))?r:"")+'              </div>\n              <div\n                class="col-md-6 col-lg-6 col-md-offset-3 col-lg-offset-3 colalert alert-warning alertModelWillBeSaved"\n                role="alert">\n                <b>'+d(o(t(668)).call(c,"_warning",{name:"L",hash:{},data:s,loc:{start:{line:24,column:19},end:{line:24,column:35}}}))+"</b> "+d(o(t(668)).call(c,"model_will_be_saved",{name:"L",hash:{},data:s,loc:{start:{line:24,column:40},end:{line:24,column:67}}}))+'\n              </div>\n            </div>\n            <div class="row progressPublishToMyPyplan nodisplay">\n              <div><b>'+d(o(t(668)).call(c,"this_may_take_a_few_minutes",{name:"L",hash:{},data:s,loc:{start:{line:28,column:22},end:{line:28,column:57}}}))+'</b></div>\n              <div class="progress progress-striped active ">\n                <div class="progress-bar" style="width: 100%;">\n                </div>\n              </div>\n            </div>\n            <div class="row externalLinkRow">\n              <div class="row">\n                <div class="col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">\n                  <input class="publishedItemLinkInput" disabled="true" />\n                </div>\n              </div>\n              <div class="row">\n                <div class="col-md-2 col-lg-2 col-md-offset-5 col-lg-offset-5">\n                  <button class="btn btn-small btnCopyToClipboard" data-placement="top" rel="tooltip"\n                    data-title="'+d(o(t(668)).call(c,"copy_to_clipboard",{name:"L",hash:{},data:s,loc:{start:{line:43,column:32},end:{line:43,column:57}}}))+'"><i class="fad fa-copy" /></button>\n                  <button class="btn btn-small btnOpenExternalLink" data-placement="top" rel="tooltip"\n                    data-title="'+d(o(t(668)).call(c,"open_link_new_window",{name:"L",hash:{},data:s,loc:{start:{line:45,column:32},end:{line:45,column:60}}}))+'"><i class="fad fa-external-link-alt" /></button>\n                </div>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class="modal-footer">\n'+(null!=(r=u(a,"each").call(c,null!=e?u(e,"buttons"):e,{name:"each",hash:{},fn:n.program(5,s,0),inverse:n.noop,data:s,loc:{start:{line:54,column:8},end:{line:57,column:17}}}))?r:"")+"      </div>\n    </div>\n  </div>\n</div>"},useData:!0})},854:function(n,e,t){"use strict";(function(a){var o,l=t(679);void 0===(o=function(){return a.Model.extend({url:"inputModule",defaults:{formsViewList:[]},search:function(n,e){(0,l.send)("reportManager/search/?text=".concat(n),null,{type:"GET"},e)},getMyReports:function(n,e){(0,l.send)("reportManager/myReports/?parent=".concat(n),null,{type:"GET"},e)},getFavsReports:function(n,e){(0,l.send)("reportManager/myReports/?favs=true",null,{type:"GET"},e)},getReportsSharedWithMe:function(n,e){(0,l.send)("reportManager/sharedWithMe/?parent=".concat(n),null,{type:"GET"},e)},getMySharedReports:function(n,e){(0,l.send)("reportManager/mySharedReports/",null,{type:"GET"},e)},getRecentsReports:function(n,e){(0,l.send)("reportManager/recents/?parent=".concat(n),null,{type:"GET"},e)},exportDashboards:function(n,e){var a=new XMLHttpRequest;a.responseType="arraybuffer",a.open("PUT","".concat(__apiURL,"/reportManager/exportItems/"),!0),a.setRequestHeader("Authorization","Token ".concat(__currentToken)),a.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),a.setRequestHeader("Content-type","application/json"),a.onreadystatechange=function(n){var a=n.currentTarget;a.readyState==a.DONE&&(200==a.status?e(a):t.e(18).then((function(){var n=[t(665)];(function(n){(new n).show({title:"ERROR!",text:a.response,notifyType:"error"})}).apply(null,n)})).catch(t.oe))},a.send(JSON.stringify(n))},exportItemsAndPublish:function(n,e,t,a,o,s,r){(0,l.send)("reportManager/exportItemsAndPublish/",JSON.stringify({username:n,uuid:e,model_folder:t,model_id:a,dashboard_ids:o,report_ids:s}),{type:"PUT",contentType:"application/json;charset=utf-8"},r)},importDashboards:function(n,e){(0,l.send)("reportManager/importItems/",JSON.stringify(n),{type:"PUT",contentType:"application/json;charset=utf-8"},e)},create:function(n,e){(0,l.send)("reportManager/",n,{type:"POST"},(function(n){null!=e&&e(n)}))},createReport:function(n,e){(0,l.send)("reportManager/",n,{type:"POST"},(function(n){null!=e&&e(n)}))},dropOnReport:function(n,e){(0,l.send)("reportManager/dropOnReport/",JSON.stringify(n),{type:"PUT",contentType:"application/json;charset=utf-8"},e)},updateOrder:function(n){(0,l.send)("reportManager/changeOrder/",JSON.stringify({values:n}),{type:"PUT",contentType:"application/json;charset=utf-8"},(function(n){}))},setAsFav:function(n,e,t){(0,l.send)("reportManager/setAsFav/",JSON.stringify({report_ids:n.report_ids,dashboard_ids:n.dashboard_ids,is_fav:e}),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},t)},updateName:function(n,e,t){(0,l.send)("reportManager/".concat(n,"/"),{name:e},{type:"PUT",dataType:"text"},(function(n){null!=t&&t(n)}))},deleteItems:function(n,e){(0,l.send)("reportManager/bulkDelete/",JSON.stringify({values:n}),{type:"DELETE",contentType:"application/json;charset=utf-8"},(function(n){null!=e&&e(n)}))},createTempId:function(){return"tmp-".concat(parseInt(5e5*Math.random()))},copyToMyReports:function(n,e){(0,l.send)("reportManager/copyToMyReports/",JSON.stringify(n),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},(function(n){null!=e&&e(n)}))},duplicateItems:function(n,e){(0,l.send)("reportManager/duplicateItems/",JSON.stringify(n),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},(function(n){e&&e(n)}))}})}.apply(e,[]))||(n.exports=o)}).call(this,t(219))}}]);