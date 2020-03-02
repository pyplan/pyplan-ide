/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[57],{219:function(e,n,t){"use strict";(function(o,a){var s,i=t(18),r=t(693);void 0===(s=function(){var e=function(e,n,t,a){if(__currentSession.modelInfo=e,o("#licenceExpiration").hide(),__currentSession.modelInfo.daysToExpire)try{var s=parseInt(__currentSession.modelInfo.daysToExpire)-1;s>=0&&s<15&&(s>=0?o("#licenceExpiration span").html((0,i.translate)("days_to_expire").replace("#days#",s)):o("#licenceExpiration span").html((0,i.translate)("license_expired")),o("#licenceExpiration").show(),setTimeout(function(){o("#licenceExpiration").hide()},15e3))}catch(e){}if(""!=e.new_session_key&&(__currentSession.session_key=e.new_session_key,(0,r.ajaxSetup)()),n(e),o(".wikiLink").attr("href","http://docs.pyplan.org"),t||o("#summary").trigger("refresh"),o("#navigation .modelopened").show(),o("#left .navigation .modelopened").show(),o("#currentModel").html(e.uri.substring(e.uri.lastIndexOf("/")+1,e.uri.lastIndexOf("."))),e.useSnapshot){var d=(0,i.translate)("use_snapshot");o("#navigation .snapshotactive").show().attr("title",d).attr("data-snapdate",e.snapshotDate)}var c=o("#navigation li.modelopened[data-key='btnSaveModelAs'] a"),l=o("#navigation li.modelopened[data-key='btnSaveModelAs'] a i");a.canEdit()?(o("#navigation li.modelopened[data-key='btnSaveModel']").show(),l.removeClass("fa-paste").addClass("fa-save-all"),c.prop("title",(0,i.translate)("save_model_as")),o("#navigation li.modelopened[data-key='btnSaveModelAs']").show(),__currentSession.modelInfo&&__currentSession.modelInfo.readonly&&(o("#navigation li.modelopened[data-key='btnSaveModel']").hide(),(0,i.showMessage)(__currentSession.modelInfo.readOnlyReason,"","info",!1))):(o("#navigation li.modelopened[data-key='btnSaveModel']").hide(),a.isInPublic(),o("#navigation li.modelopened[data-key='btnSaveModelAs']").hide())};return a.Model.extend({openModel:function(n,t,a,s){o("#navigation .snapshotactive").hide();var i=this;(0,r.send)("modelManager/openModel/",{file:n},null,function(n){n&&e(n,t,a,i)},s)},createNewModel:function(n,t,a,s){o("#navigation .snapshotactive").hide();var i=this;(0,r.send)("modelManager/createNewModel/",{modelName:n},null,function(n){n&&e(n,t,a,i)},s)},closeModel:function(e){(0,r.send)("modelManager/closeModel/",null,null,function(){Promise.all([t.e(2),t.e(4),t.e(61)]).then(function(){var n=[t(684)];(function(n){(new n).clearUI(),e()}).apply(null,n)}).catch(t.oe)})},saveModel:function(e){(0,r.send)("modelManager/saveModel/",null,{dataType:"text"},function(){e()})},saveModelAs:function(e,n){(0,r.send)("modelManager/saveModelAs/",{name:e},{type:"GET"},function(e){n(e)})},saveModelToMyWorkspace:function(e,n,t,o){(0,r.send)("modelManager/saveModelToMyWorkspace/?source=".concat(encodeURIComponent(e),"&name=").concat(n,"&fileLocation=").concat(encodeURIComponent(t)),null,{type:"GET",dataType:"text"},o)},getModelInfo:function(e){(0,r.send)("modelManager/getModelInfo/",null,null,e)},isInPublic:function(){return!!(__currentSession.modelInfo.uri&&__currentSession.modelInfo.uri.toLowerCase().indexOf("/public/")>=0)},canEdit:function(){var e=!1,n=this.isInPublic();return((0,i.haveAccess)("change_model")&&!n||(0,i.haveAccess)("change_public_model")&&n)&&(e=!0),e},setModelPreferences:function(e,n,t,a){(0,r.send)("modelManager/setModelPreferences/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){void 0!=n&&n(e),o("body").trigger("pendingChanges",[!0])},function(e){t(e)},!1,a)},getModelPreferences:function(e,n,t){(0,r.send)("modelManager/getModelPreferences/",null,{type:"GET"},e,n,!0,t)},setNodeProperties:function(e,n,t,a,s,i){void 0===i&&(i=!0),(0,r.send)("modelManager/setNodeProperties/",JSON.stringify({node:e,properties:n}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){void 0!=t&&t(e),o("body").trigger("pendingChanges",[i])},function(e){a(e)},!1,s)},setNodesProperties:function(e,n){(0,r.send)("modelManager/setNodesProperties/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){n(e),o("body").trigger("pendingChanges",[!0])})},setNodeIdFromTitle:function(e,n){(0,r.send)("modelManager/setNodeIdFromTitle/",{value:e},{type:"POST"},function(e){n(e),o("body").trigger("pendingChanges",[!0])})},getNodeProperties:function(e,n,t,o,a,s){(0,r.send)("modelManager/getNodeProperties/",JSON.stringify({node:e,properties:n,forceThisNode:s}),{type:"POST",contentType:"application/json;charset=utf-8"},t,o,!0,a)},getInputs:function(e,n){(0,r.send)("modelManager/getNodeInputs/?node="+e,null,{type:"GET"},n)},getOutputs:function(e,n){(0,r.send)("modelManager/getNodeOutputs/?node="+e,null,{type:"GET"},n)},executeForRefresh:function(e){(0,r.send)("modelManager/executeForRefresh/",null,{type:"POST",dataType:"text"},function(n){void 0!=e&&e(n)})},createNode:function(e,n,t){(0,r.send)("modelManager/createNode/",e,{type:"POST"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},createAlias:function(e,n,t){(0,r.send)("modelManager/createAlias/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},createInputNode:function(e,n,t){(0,r.send)("modelManager/createInputNode/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},deleteNodes:function(e,n,t){(0,r.send)("modelManager/deleteNodes/",JSON.stringify({values:e}),{type:"DELETE",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},searchNode:function(e,n,t){var o=e.text,a=void 0===o?"":o,s=e.extraClasses,i=void 0===s?[]:s,d=e.moduleId,c=e.nodeClass,l=e.fillDetail;(0,r.send)("modelManager/searchNodes/?text=".concat(a).concat(d?"&moduleId=".concat(d):"").concat(c?"&nodeClass=".concat(c):"").concat(l?"&fillDetail=".concat(l):""),JSON.stringify({extraClasses:i}),{type:"POST",contentType:"application/json;charset=utf-8"},n,t)},SearchForAutocomplete:function(e,n,t){(0,r.send)("modelManager/searchForAutocomplete/",{text:e},{type:"GET",dataType:"text"},n,t)},navigateDiagram:function(e,n,t){(0,r.send)("modelManager/navigateDiagram/",{moduleId:e,includeArrows:!1},null,n,t)},getArrows:function(e,n,t){(0,r.send)("modelManager/getArrows/",{moduleId:e},null,n,t)},executeButton:function(e,n,t){(0,r.send)("modelManager/executeButton/",JSON.stringify({nodeId:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,t)},evaluateNode:function(e,n,t){(0,r.send)("dashboardManager/getOrCreate/",{node:e},void 0,n,t)},isInBackground:function(e,n,t){(0,r.send)("modelManager/isInBackground/",{nodeId:e},{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n,t,!0)},abortProcess:function(e,n){(0,r.send)("modelManager/abortProcess/",null,{type:"GET"},e,n)},getIndexValues:function(e,n){(0,r.send)("dashboardManager/getIndexValues/",e,null,function(e){e&&n(e)})},getNodeIndexes:function(e,n){(0,r.send)("dashboardManager/getNodeIndexes/",{node:e},null,function(e){e&&n(e)})},getSelector:function(e,n){(0,r.send)("modelManager/getSelector/",{node:e},{type:"POST"},n)},exportFlatNode:function(e,n,o,a,s,i){var r={nodeId:e,fileFormat:n,numberFormat:o,columnFormat:a,compressed:s},d=new XMLHttpRequest;d.responseType="arraybuffer",d.open("POST","".concat(__apiURL,"/modelManager/exportFlatNode/")),d.setRequestHeader("Authorization","Token ".concat(__currentToken)),d.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),d.setRequestHeader("Content-type","application/json;charset=utf-8"),d.onreadystatechange=function(e){var n=e.currentTarget;n.readyState==n.DONE&&(200==n.status?i(n):Promise.all([t.e(2),t.e(18)]).then(function(){var e=[t(685)];(function(e){(new e).show({title:"ERROR!",text:n.response,notifyType:"error"})}).apply(null,e)}).catch(t.oe))},d.send(JSON.stringify(r))},exportCurrentNode:function(e,n,o,a,s,i,r){var d={nodeId:e,fileFormat:n,numberFormat:o,columnFormat:a,compressed:s,nodeQuery:i},c=new XMLHttpRequest;c.responseType="arraybuffer",c.open("POST","".concat(__apiURL,"/modelManager/exportCurrentNode/")),c.setRequestHeader("Authorization","Token ".concat(__currentToken)),c.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),c.setRequestHeader("Content-type","application/json;charset=utf-8"),c.onreadystatechange=function(e){var n=e.currentTarget;n.readyState==n.DONE&&(200==n.status?r(n):Promise.all([t.e(2),t.e(18)]).then(function(){var e=[t(685)];(function(e){(new e).show({title:"ERROR!",text:n.response,notifyType:"error"})}).apply(null,e)}).catch(t.oe))},c.send(JSON.stringify(d))},getDepartments:function(e,n){(0,r.send)("departments/by_current_company/",null,{type:"GET"},e,n)},getDeniedDepartments:function(e,n){(0,r.send)("departments/denied/?module=".concat(e),null,{type:"GET"},n)},setDeniedModule:function(e,n){(0,r.send)("departments/deny_items/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8"},n)},openParallelModel:function(e,n){(0,r.send)("ModelManager/openParallelModel/?file="+e,null,{type:"GET"},n)},closeParallelModel:function(e,n){(0,r.send)("ModelManager/closeParallelModel/?parallelToken="+e,null,{type:"GET"},n)},moveNodes:function(e,n,t){(0,r.send)("modelManager/moveNodes/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},copyNodes:function(e,n,t){(0,r.send)("modelManager/copyNodes/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},copyAsValues:function(e,n,t,a){(0,r.send)("modelManager/copyAsValues/",JSON.stringify({nodeId:e,asNewNode:n}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=t&&t(e)},a)},setNodePosition:function(e,n,t){(0,r.send)("modelManager/setNodesPosition/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},setNodeSize:function(e,n,t){(0,r.send)("modelManager/setNodesSize/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},setNodeZ:function(e,n,t){(0,r.send)("modelManager/setNodeZ/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},changeSession:function(n,o){var a=this;(0,r.send)("modelManager/changeToOtherModelSession/",{new_session_key:n},null,function(n){Promise.all([t.e(2),t.e(4),t.e(61)]).then(function(){var s=[t(684)];(function(t){(new t).clearUI(),e(n,o,!0,a)}).apply(null,s)}).catch(t.oe)})},getSharedNode:function(e,n){(0,r.send)("result/by_node_id/".concat(e,"/"),null,{type:"GET"},function(e){e&&n(e)},function(e,t){e&&n&&n(e)})},setSharedNode:function(e,n){(0,r.send)("result/".concat(e.id,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8"},function(e){e&&n&&n(e)})},exportModuleToFile:function(e,n,t,o){var a={moduleId:e,exportType:n},s=new XMLHttpRequest;s.responseType="arraybuffer",s.open("POST","".concat(__apiURL,"/modelManager/exportModuleToFile/")),s.setRequestHeader("Authorization","Token ".concat(__currentToken)),s.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),s.setRequestHeader("Content-type","application/json;charset=utf-8"),s.onreadystatechange=function(e){var n=e.currentTarget;n.readyState==n.DONE&&(200==n.status?t(n):o(n.response))},s.send(JSON.stringify(a))},importModuleFromFile:function(e,n,t){(0,r.send)("modelManager/importModuleFromFile/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},function(e){o("body").trigger("pendingChanges",[!0]),void 0!=n&&n(e)},t)},getProfile:function(e,n,t,o){(0,r.send)("modelManager/getNodeProfile/",{nodeId:e},{type:"GET"},n,t,!0,o)},previewNode:function(e,n,t){var o={node:e};(0,r.send)("modelManager/previewNode/",o,{type:"POST"},n,t)},stopProcess:function(e,n){(0,r.send)("modelManager/stop/",null,{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},e,n,!1,!1)},listShortcuts:function(e){(0,r.send)("diagramShortcut/",null,{type:"GET"},e)},createShortcut:function(e,n){(0,r.send)("diagramShortcut/?node_id=".concat(e),null,{type:"POST"},function(e){void 0!=n&&n(e)})},deleteShortcut:function(e,n){(0,r.send)("diagramShortcut/".concat(e,"/"),null,{type:"DELETE"},function(e){void 0!=n&&n(e)})},getToolbars:function(e){(0,r.send)("modelManager/getToolbars/",null,{type:"GET"},e)},callWizard:function(e,n,t){(0,r.send)("modelManager/callWizard/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,t)},getFilesForImportWizard:function(e,n){(0,r.send)("modelManager/getFilesForImportWizard/",{extension:e},{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},installLibrary:function(e,n){(0,r.send)("modelManager/installLibrary/",JSON.stringify({lib:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n)},listInstalledLibraries:function(e){(0,r.send)("modelManager/listInstalledLibraries/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},e)},uninstallLibrary:function(e,n,t){(0,r.send)("modelManager/uninstallLibrary/",JSON.stringify({lib:e,target:n}),{type:"DELETE",contentType:"application/json;charset=utf-8",dataType:"text"},t)},getInstallProgress:function(e,n,t){(0,r.send)("modelManager/getInstallProgress/",{from_line:e},{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n,t,!0,!0)}})}.apply(n,[]))||(e.exports=s)}).call(this,t(1),t(218))}}]);