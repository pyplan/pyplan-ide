/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[124,30,36,45,85,150,151,182,185,222,223,224],{220:function(e,n,t){"use strict";(function(o,a){var s,r,i=t(18),c=t(679);s=[t(666)],void 0===(r=function(e){var n=function(n,t,a,s){if(__currentSession.modelInfo=n,o("#licenceExpiration").hide(),__currentSession.modelInfo.daysToExpire)try{var r=parseInt(__currentSession.modelInfo.daysToExpire)-1;r>=0&&r<15&&(r>=0?o("#licenceExpiration span").html((0,i.translate)("days_to_expire").replace("#days#",r)):o("#licenceExpiration span").html((0,i.translate)("license_expired")),o("#licenceExpiration").show(),setTimeout((function(){o("#licenceExpiration").hide()}),15e3))}catch(e){}if(""!=n.new_session_key){var l=__currentSession.session_key;__currentSession.session_key=n.new_session_key,(0,c.ajaxSetup)(),(new e).changeSessionKey(l,__currentSession.session_key)}if(t(n),o(".wikiLink").attr("href","http://docs.pyplan.org"),a||o("#summary").trigger("refresh"),o("#navigation .modelopened").show(),o("#left .navigation .modelopened").show(),o("#currentModel").html(n.uri.substring(n.uri.lastIndexOf("/")+1,n.uri.lastIndexOf("."))),n.useSnapshot){var u=(0,i.translate)("use_snapshot");o("#navigation .snapshotactive").show().attr("title",u).attr("data-snapdate",n.snapshotDate)}var d=o("#navigation li.modelopened[data-key='btnSaveModelAs'] a"),p=o("#navigation li.modelopened[data-key='btnSaveModelAs'] a i");s.canEdit()?(o("#navigation li.modelopened[data-key='btnSaveModel']").show(),p.removeClass("fa-paste").addClass("fa-save-all"),d.prop("title",(0,i.translate)("save_model_as")),o("#navigation li.modelopened[data-key='btnSaveModelAs']").show(),__currentSession.modelInfo&&__currentSession.modelInfo.readonly&&(o("#navigation li.modelopened[data-key='btnSaveModel']").hide(),(0,i.showMessage)(__currentSession.modelInfo.readOnlyReason,(0,i.translate)("_read_only"),"error",!1))):(o("#navigation li.modelopened[data-key='btnSaveModel']").hide(),s.isInPublic(),o("#navigation li.modelopened[data-key='btnSaveModelAs']").hide())};return a.Model.extend({openModel:function(e,t,a,s){o("#navigation .snapshotactive").hide();var r=this;(0,c.send)("modelManager/openModel/",{file:e},null,(function(e){e&&n(e,t,a,r)}),s)},createNewModel:function(e,t,a,s){o("#navigation .snapshotactive").hide();var r=this;(0,c.send)("modelManager/createNewModel/",{modelName:e},null,(function(e){e&&n(e,t,a,r)}),s)},closeModel:function(e){(0,c.send)("modelManager/closeModel/",null,null,(function(){Promise.all([t.e(2),t.e(4),t.e(85)]).then((function(){var n=[t(664)];(function(n){(new n).clearUI(),e()}).apply(null,n)})).catch(t.oe)}))},saveModel:function(e){(0,c.send)("modelManager/saveModel/",null,{dataType:"text"},(function(){e()}))},saveModelAs:function(e,n){(0,c.send)("modelManager/saveModelAs/",{name:e},{type:"GET"},(function(e){n(e)}))},saveModelToMyWorkspace:function(e,n,t,o){(0,c.send)("modelManager/saveModelToMyWorkspace/?source=".concat(encodeURIComponent(e),"&name=").concat(n,"&fileLocation=").concat(encodeURIComponent(t)),null,{type:"GET",dataType:"text"},o)},getModelInfo:function(e){(0,c.send)("modelManager/getModelInfo/",null,null,e)},isInPublic:function(){return!!(__currentSession.modelInfo.uri&&__currentSession.modelInfo.uri.toLowerCase().indexOf("/public/")>=0)},canEdit:function(){var e=!1,n=this.isInPublic();return((0,i.haveAccess)("change_model")&&!n||(0,i.haveAccess)("change_public_model")&&n)&&(e=!0),e},setModelPreferences:function(e,n,t,a){(0,c.send)("modelManager/setModelPreferences/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){null!=n&&n(e),o("body").trigger("pendingChanges",[!0])}),(function(e){t(e)}),!1,a)},getModelPreferences:function(e,n,t){(0,c.send)("modelManager/getModelPreferences/",null,{type:"GET"},e,n,!0,t)},setNodeProperties:function(e,n,t,a,s,r){void 0===r&&(r=!0),(0,c.send)("modelManager/setNodeProperties/",JSON.stringify({node:e,properties:n}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){null!=t&&t(e),o("body").trigger("pendingChanges",[r])}),(function(e){a(e)}),!1,s)},setNodesProperties:function(e,n){(0,c.send)("modelManager/setNodesProperties/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){n(e),o("body").trigger("pendingChanges",[!0])}))},setNodeIdFromTitle:function(e,n){(0,c.send)("modelManager/setNodeIdFromTitle/",{value:e},{type:"POST"},(function(e){n(e),o("body").trigger("pendingChanges",[!0])}))},getNodeProperties:function(e,n,t,o,a,s){(0,c.send)("modelManager/getNodeProperties/",JSON.stringify({node:e,properties:n,forceThisNode:s}),{type:"POST",contentType:"application/json;charset=utf-8"},t,o,!0,a)},getInputs:function(e,n){(0,c.send)("modelManager/getNodeInputs/?node="+e,null,{type:"GET"},n)},getOutputs:function(e,n){(0,c.send)("modelManager/getNodeOutputs/?node="+e,null,{type:"GET"},n)},executeForRefresh:function(e){(0,c.send)("modelManager/executeForRefresh/",null,{type:"POST",dataType:"text"},(function(n){null!=e&&e(n)}))},createNode:function(e,n,t){(0,c.send)("modelManager/createNode/",e,{type:"POST"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},createAlias:function(e,n,t){(0,c.send)("modelManager/createAlias/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},createInputNode:function(e,n,t){(0,c.send)("modelManager/createInputNode/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},deleteNodes:function(e,n,t){(0,c.send)("modelManager/deleteNodes/",JSON.stringify({values:e}),{type:"DELETE",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},searchNode:function(e,n,t){var o=e.text,a=void 0===o?"":o,s=e.extraClasses,r=void 0===s?[]:s,i=e.moduleId,l=e.nodeClass,u=e.fillDetail;(0,c.send)("modelManager/searchNodes/?text=".concat(a).concat(i?"&moduleId=".concat(i):"").concat(l?"&nodeClass=".concat(l):"").concat(u?"&fillDetail=".concat(u):""),JSON.stringify({extraClasses:r}),{type:"POST",contentType:"application/json;charset=utf-8"},n,t)},SearchForAutocomplete:function(e,n,t){(0,c.send)("modelManager/searchForAutocomplete/",{text:e},{type:"GET",dataType:"text"},n,t)},navigateDiagram:function(e,n,t){(0,c.send)("modelManager/navigateDiagram/",{moduleId:e,includeArrows:!1},null,n,t)},getArrows:function(e,n,t){(0,c.send)("modelManager/getArrows/",{moduleId:e},null,n,t)},executeButton:function(e,n,t){(0,c.send)("modelManager/executeButton/",JSON.stringify({nodeId:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,t)},evaluateNode:function(e,n,t){(0,c.send)("dashboardManager/getOrCreate/",{node:e},void 0,n,t)},abortProcess:function(e,n){(0,c.send)("modelManager/abortProcess/",null,{type:"GET"},e,n)},getIndexValues:function(e,n){(0,c.send)("dashboardManager/getIndexValues/",e,null,(function(e){e&&n(e)}))},getNodeIndexes:function(e,n){(0,c.send)("dashboardManager/getNodeIndexes/",{node:e},null,(function(e){e&&n(e)}))},getSelector:function(e,n){(0,c.send)("modelManager/getSelector/",{node:e},{type:"POST"},n)},exportFlatNode:function(e,n,o,a,s,r){var i={nodeId:e,fileFormat:n,numberFormat:o,columnFormat:a,compressed:s},c=new XMLHttpRequest;c.responseType="arraybuffer",c.open("POST","".concat(__apiURL,"/modelManager/exportFlatNode/")),c.setRequestHeader("Authorization","Token ".concat(__currentToken)),c.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),c.setRequestHeader("Content-type","application/json;charset=utf-8"),c.onreadystatechange=function(e){var n=e.currentTarget;n.readyState==n.DONE&&(200==n.status?r(n):Promise.all([t.e(2),t.e(66)]).then((function(){var e=[t(665)];(function(e){(new e).show({title:"ERROR!",text:n.response,notifyType:"error"})}).apply(null,e)})).catch(t.oe))},c.send(JSON.stringify(i))},exportCurrentNode:function(e,n,o,a,s,r,i){var c={nodeId:e,fileFormat:n,numberFormat:o,columnFormat:a,compressed:s,nodeQuery:r},l=new XMLHttpRequest;l.responseType="arraybuffer",l.open("POST","".concat(__apiURL,"/modelManager/exportCurrentNode/")),l.setRequestHeader("Authorization","Token ".concat(__currentToken)),l.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),l.setRequestHeader("Content-type","application/json;charset=utf-8"),l.onreadystatechange=function(e){var n=e.currentTarget;n.readyState==n.DONE&&(200==n.status?i(n):Promise.all([t.e(2),t.e(66)]).then((function(){var e=[t(665)];(function(e){(new e).show({title:"ERROR!",text:n.response,notifyType:"error"})}).apply(null,e)})).catch(t.oe))},l.send(JSON.stringify(c))},getDepartments:function(e,n){(0,c.send)("departments/by_current_company/",null,{type:"GET"},e,n)},getDeniedDepartments:function(e,n){(0,c.send)("departments/denied/?module=".concat(e),null,{type:"GET"},n)},setDeniedModule:function(e,n){(0,c.send)("departments/deny_items/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8"},n)},openParallelModel:function(e,n){(0,c.send)("ModelManager/openParallelModel/?file="+e,null,{type:"GET"},n)},closeParallelModel:function(e,n){(0,c.send)("ModelManager/closeParallelModel/?parallelToken="+e,null,{type:"GET"},n)},moveNodes:function(e,n,t){(0,c.send)("modelManager/moveNodes/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},copyNodes:function(e,n,t){(0,c.send)("modelManager/copyNodes/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},copyAsValues:function(e,n,t,a){(0,c.send)("modelManager/copyAsValues/",JSON.stringify({nodeId:e,asNewNode:n}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=t&&t(e)}),a)},setNodePosition:function(e,n,t){(0,c.send)("modelManager/setNodesPosition/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},setNodeSize:function(e,n,t){(0,c.send)("modelManager/setNodesSize/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},setNodeZ:function(e,n,t){(0,c.send)("modelManager/setNodeZ/",JSON.stringify({values:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},changeSession:function(e,o){var a=this;(0,c.send)("modelManager/changeToOtherModelSession/",{new_session_key:e},null,(function(e){Promise.all([t.e(2),t.e(4),t.e(85)]).then((function(){var s=[t(664)];(function(t){(new t).clearUI(),n(e,o,!0,a)}).apply(null,s)})).catch(t.oe)}))},getSharedNode:function(e,n){(0,c.send)("result/by_node_id/".concat(e,"/"),null,{type:"GET"},(function(e){e&&n(e)}),(function(e,t){e&&n&&n(e)}))},setSharedNode:function(e,n){(0,c.send)("result/".concat(e.id,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8"},(function(e){e&&n&&n(e)}))},exportModuleToFile:function(e,n,t,o){var a={moduleId:e,exportType:n},s=new XMLHttpRequest;s.responseType="arraybuffer",s.open("POST","".concat(__apiURL,"/modelManager/exportModuleToFile/")),s.setRequestHeader("Authorization","Token ".concat(__currentToken)),s.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),s.setRequestHeader("Content-type","application/json;charset=utf-8"),s.onreadystatechange=function(e){var n=e.currentTarget;n.readyState==n.DONE&&(200==n.status?t(n):o(n.response))},s.send(JSON.stringify(a))},importModuleFromFile:function(e,n,t){(0,c.send)("modelManager/importModuleFromFile/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},(function(e){o("body").trigger("pendingChanges",[!0]),null!=n&&n(e)}),t)},getProfile:function(e,n,t,o){(0,c.send)("modelManager/getNodeProfile/",{nodeId:e},{type:"GET"},n,t,!0,o)},previewNode:function(e,n,t,o){var a={node:e,debugMode:o};(0,c.send)("modelManager/previewNode/",a,{type:"POST"},n,t)},stopProcess:function(e,n){(0,c.send)("modelManager/stop/",null,{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},e,n,!1,!1)},listShortcuts:function(e){(0,c.send)("diagramShortcut/",null,{type:"GET"},e)},createShortcut:function(e,n){(0,c.send)("diagramShortcut/?node_id=".concat(e),null,{type:"POST"},(function(e){null!=n&&n(e)}))},deleteShortcut:function(e,n){(0,c.send)("diagramShortcut/".concat(e,"/"),null,{type:"DELETE"},(function(e){null!=n&&n(e)}))},callWizard:function(e,n,t){(0,c.send)("modelManager/callWizard/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n,t)},getFilesForImportWizard:function(e,n){(0,c.send)("modelManager/getFilesForImportWizard/",{extension:e},{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n)},installLibrary:function(e,n){(0,c.send)("modelManager/installLibrary/",JSON.stringify({lib:e}),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},n)},listInstalledLibraries:function(e){(0,c.send)("modelManager/listInstalledLibraries/",null,{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},e)},uninstallLibrary:function(e,n,t){(0,c.send)("modelManager/uninstallLibrary/",JSON.stringify({lib:e,target:n}),{type:"DELETE",contentType:"application/json;charset=utf-8",dataType:"text"},t)},getInstallProgress:function(e,n,t){(0,c.send)("modelManager/getInstallProgress/",{from_line:e},{type:"GET",contentType:"application/json;charset=utf-8",dataType:"text"},n,t,!0,!0)}})}.apply(n,s))||(e.exports=r)}).call(this,t(1),t(219))},666:function(e,n,t){"use strict";(function(o,a){var s,r,i=t(18);function c(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}var l=(c(r={},0,"info"),c(r,1,"success"),c(r,2,"error"),c(r,3,"warning"),r);void 0===(s=function(){return o.Controller.extend({name:"ws",socket:void 0,changeSessionKey:function(e,n){this.socket?(this.socket.send(JSON.stringify({command:"leave",room:e,message:"Leaving!"})),this.socket.send(JSON.stringify({command:"join",room:n,message:"Joining!"}))):this.start()},start:function(){var e=__currentSession.company_code;this.socket=new WebSocket("".concat(__wsURL,"/notifications/").concat(e,"/?apiKey=").concat(__currentToken)),this.events()},events:function(){var e=this,n=__currentSession.session_key;this.socket.onopen=function(t){e.socket.send(JSON.stringify({command:"join",room:n,message:"Joining!"}))},this.socket.onmessage=this.processMessage,this.socket.onclose=function(n){console.log("Client notified socket has closed",n),setTimeout((function(){e.start()}),5e3)}},triggerEvent:function(e,n){this.socket&&this.socket.connected&&this.socket.send({type:e,session_key:__currentSession.session_key,message:n})},processMessage:function(e){var n,o=function(e){(0,i.showMessage)(e.message?(0,i.translate)(e.message):"",e.title?(0,i.translate)(e.title):"",e.not_level?l[e.not_level]:"info",-1,!1)},s=(c(n={},0,(function(e){o(e)})),c(n,1,(function(e){o(e),setTimeout((function(){location.reload()}),2e3)})),c(n,4,(function(e){!function(e){Promise.all([t.e(2),t.e(4),t.e(54)]).then((function(){var n=[t(682)];(function(n){(new n).showProgressBar(e)}).apply(null,n)})).catch(t.oe)}(e)})),c(n,5,(function(e){a("#main-modal").trigger("progress",e)})),c(n,6,(function(e){a("#main-modal").trigger("debug_info",e)})),n);if(e){var r=JSON.parse(e.data);r&&(r.title||r.message||r.node||"number"==typeof r.progress)&&"number"==typeof r.msg_type&&s[r.msg_type]&&s[r.msg_type](r)}},to_delete_processMessage:function(e){if(e){var n=JSON.parse(e.data);switch(n.msg_type){case"MemoryQuotaExceeded":a("body").trigger("memoryQuotaExceeded",[n.body]);break;case"ProcessCancelByMemoryQuotaExceeded":var o=(0,i.translate)("process_cancel_by_quota").replace("##quota##",n.body.memoryQuota).replace("##current##",n.body.modelMemory);(0,i.showMessage)(o,(0,i.translate)("_canceled"),"error");break;case"modelmsgbox":Promise.all([t.e(2),t.e(4),t.e(54)]).then((function(){var e=[t(682)];(function(e){(new e).showMsgBox(n.body)}).apply(null,e)})).catch(t.oe);break;case"DashboardShareAfterSave":a("#model-summary").trigger("reloadShared",[n.body]);break;case"loadInputTemplate":case"unloadInputTemplate":case"setInputTemplatePos":case"setInputTemplateValues":a(".inputFormTask").trigger("collabMessage",[n.event,n.body]);break;case"ModelEditionAvailable":n&&n.body&&n.body.message&&((0,i.showMessage)(n.body.message,(0,i.translate)("_edition_available"),"info"),__currentSession.modelInfo&&__currentSession.modelInfo.uri==n.body.modelfile&&t.e(223).then((function(){var e=[t(220)];(function(e){(new e).canEdit()&&(a("#navigation li.modelopened[data-key='btnSaveModel']").show(),a("#navigation li.modelopened[data-key='btnSaveModelAs']").show())}).apply(null,e)})).catch(t.oe))}}}})}.apply(n,[]))||(e.exports=s)}).call(this,t(677),t(1))},677:function(e,n,t){var o,a;!function(s,r){if(!s.BackboneMVC){var i=s.BackboneMVC={};o=[t(219),t(221),t(1)],void 0===(a=function(e,n,t){return function(e,n,t,o,a){"use strict";if(void 0===t||void 0===o)return;var s=function(){function e(){this._created=(new Date).getTime()}return o.extend(e.prototype,{_created:null}),e.extend=function(n){var t,a=function(){return void 0!==t?t:(e.apply(this,arguments),void 0!==this.initialize&&this.initialize.apply(this,arguments),t=this)};return a.prototype=new e,o.extend(a.prototype,n),a.prototype.constructor=a,a.prototype.classId=o.uniqueId("controller_"),a},e}();o.extend(n,{namespace:function(n){for(var t=n.split("."),o=e,a=0,s=t.length;a<s;a++)void 0===o[t[a]]&&(o[t[a]]={}),o=o[t[a]]},Controller:{beforeFilter:function(){return(new a.Deferred).resolve()},afterRender:function(){return(new a.Deferred).resolve()},checkSession:function(){return(new a.Deferred).resolve(!0)},default:function(){return!0}},Router:function(){var e={_history:[],routes:{"*components":"dispatch"},dispatch:function(e){var n,t=(e||"").replace(/\/+$/g,"").split("/");if(r[t[0]]?n=t[0]:void 0!==r[u(t[0])]?n=u(t[0]):void 0!==r[d(t[0])]&&(n=d(t[0])),void 0===n)return this[404]();var s=new r[n],i=t.length>1?t[1]:"default";if("function"!=typeof s._actions[i])return this[404]();var p=t.length>2?o.rest(t,2):[];return function(e,n,t,a){e._history.length>888&&(e._history=o.last(e._history,888));e._history.push([n,t,a])}(this,n,i,p),function(e,n,t){var o=new r[e],s=[n].concat(t),i=a.Deferred(),u=o.beforeFilter.apply(o,s);c(u)?i=u:l(i,u);"function"==typeof o._secureActions[n]&&(i=i.pipe((function(){var e=o.checkSession.apply(o,t);return c(e)?e:l(new a.Deferred,e)})));return i=(i=i.pipe((function(){var e=o[n].apply(o,t);return c(e)?e:l(new a.Deferred,e)}))).pipe((function(){var e=o.afterRender.apply(o,s);return c(e)?e:l(new a.Deferred,e)}))}(n,i,p)},404:function(){},getLastAction:function(){return o.last(this._history,1)[0]},navigate:function(e,n){n&&!0!==n||(n={trigger:n});var s=o.extend({},n);return s.trigger=!1,t.Router.prototype.navigate.call(this,e,s),n.trigger?this.dispatch(e):(new a.Deferred).resolve()}};function n(n){var a=o.extend(n.routes||{},e.routes);return t.Router.extend(o.extend({},e,n,{routes:a}))}var s=t.Router.extend(o.extend({extend:n},e));return s.extend=n,s}(),Model:{extend:function(e){return e=o.extend({__fetchSuccessCallback:null,__fetchErrorCallback:null,fetch:function(e){var n=(e=e||{}).success;e.success=function(e,t){if(n&&n(e,t),e.__fetchSuccessCallback){var o=e.__fetchSuccessCallback;e.__fetchSuccessCallback=null,o.apply(e)}};var a=e.error;e.error=function(e,n){a&&a(e,n),e.trigger("error",a)},t.Model.prototype.fetch.apply(this,[e].concat(o.rest(arguments)))},parse:function(e){return this.__fetchSuccessCallback=null,this.__fetchErrorCallback=null,!e||e.error?(this.trigger("error",e&&e.error||e),{}):(this.__fetchSuccessCallback=function(){this.trigger("read",e.data)}.bind(this),e.data)}},e),t.Model.extend(e)}}}),n.Controller.extend=function e(t,a){return function(t){var c=t.name;if(void 0===c)throw"'name' property is mandatory ";t=o.extend({},a,t);var l=o.extend({},n.Controller),u={},d={};o.each(t,(function(e,n){if(l[n]=e,"function"!=typeof e||"_"===n[0]||o.indexOf(i,n)>=0)return!1;if(u[n]=e,n.match(/^user_/i)){d[n]=e;var a=n.replace(/^user_/i,"");"function"!=typeof t[a]&&(d[a]=e,u[a]=e)}})),o.extend(l,u,{_actions:u,_secureActions:d}),"extend"in l&&delete l.extend;var p=s.extend(l);return o.extend(p,{extend:e(p,o.extend({},a,t))}),r[c]=p,p}}(n.Controller,{});var r={},i=["initialize","beforeFilter","afterRender","checkSession"];function c(e){return o.isObject(e)&&e.promise&&"function"==typeof e.promise}function l(e,n){return void 0===n&&(n=!0),e[n?"resolve":"reject"](n)}function u(e){return"string"!=typeof e?null:(e=e.replace(/\s{2,}/g," "),o.map(e.split(" "),(function(e){return e.replace(/(^|_)[a-z]/gi,(function(e){return e.toUpperCase()})).replace(/_/g,"")})).join(" "))}function d(e){return"string"!=typeof e?null:(e=e.replace(/\s{2,}/g," "),o.map(e.split(" "),(function(e){return e.replace(/^[A-Z]/g,(function(e){return e.toLowerCase()})).replace(/([a-z])([A-Z])/g,(function(e,n,t){return n+"_"+t.toLowerCase()}))})).join(" "))}}(s,i,e,n,t),i}.apply(n,o))||(e.exports=a)}}(this)},679:function(e,n,t){"use strict";t.r(n),function(e){t.d(n,"ajaxSetup",(function(){return a})),t.d(n,"send",(function(){return s}));var o=t(18);function a(n=null){e.ajaxSetup({dataType:"json",crossDomain:!0,headers:{Authorization:"Token "+__currentToken,"session-key":__currentSession?__currentSession.session_key:""},...()=>n||{}})}function s(n,a,s,r,i,c,l){s||(s=new Object),c||e("#secondLoading").show(),s.hasOwnProperty("success")||(s.success=function(n,o,a){if("object"!=typeof n&&null!=n&&""!=n)try{n=e.parseJSON(n)}catch(e){}c||(e("#mainLoading").hide(),e("#secondLoading").hide());const s=function(e,n,o,a,s){e&&e.hasOwnProperty("hasError")?(o||Promise.all([t.e(2),t.e(24)]).then((function(){var n=[t(665)];(function(n){(new n).show({title:"WARNING!",text:e.error,notifyType:"error"})}).apply(null,n)})).catch(t.oe),null!=s&&s(e.error)):null!=a&&a(e,n)};n&&n.hasOwnProperty("isCompressed")&&n.hasOwnProperty("obj")?t.e(268).then((function(){var o=[t(870)];(function(t){n=e.parseJSON(t.inflate(atob(n.obj),{to:"string"})),s(n,a,l,r,i)}).apply(null,o)})).catch(t.oe):s(n,a,l,r,i)}),s.hasOwnProperty("type")||(s.type="GET"),a&&(s.data=a),s.error=function(a,r,u){if(c||(e("#mainLoading").hide(),e("#secondLoading").hide()),a){let e="";const r=`[${s.type}] ${n}`;if(a.responseJSON)for(const n in a.responseJSON)e+="non_field_errors"==n?a.responseJSON[n]+"\n":`[${n}]: ${a.responseJSON[n]}\n`;else e=a.responseText+"\n";let c="error",u=void 0,d=void 0,p=Object(o.translate)("_warning"),f=!0;const y=[];switch(a.status){case 401:d=15e3,u=()=>{location.reload()},y.push({css:"warning",code:"401",title:Object(o.translate)("relog")});break;case 403:d=1e4,p=Object(o.translate)("access_denied");break;case 406:d=0,f=!1}if(null!=i){!1===i(e,a)&&(l=!0)}null!=l&&0!=l||Promise.all([t.e(2),t.e(24)]).then((function(){var n=[t(665)];(function(n){(new n).show({title:p,text:e,endpoint:r,notifyType:c,timeOut:d,tapToDismiss:f,buttons:y,callback:u})}).apply(null,n)})).catch(t.oe)}},e.ajax({url:`${__apiURL}/${n}`,contentType:s.contentType,data:a,dataType:s.dataType?s.dataType:"json",method:s.type,success:s.success,error:s.error})}}.call(this,t(1))},719:function(e,n,t){"use strict";(function(o){var a,s=t(18),r=t(679);void 0===(a=function(){var e=function(e,n,o){null!==e.companySettingFile&&""!==e.companySettingFile&&t.e(42).then((function(){var n=[t(702)("./".concat(e.companySettingFile))];(function(){Promise.resolve().then((function(){t(222)})).catch(t.oe)}).apply(null,n)})).catch(t.oe),__currentSession=e,(0,s.setProcessDictionary)(e.process),(0,r.ajaxSetup)(),Promise.all([t.e(2),t.e(4),t.e(45)]).then((function(){var o=[t(664)];(function(t){(new t).clearUI(),n(e)}).apply(null,o)})).catch(t.oe)};return o.Model.extend({isConnected:function(){return""!=__currentToken&&null!==__currentSession},connect:function(e,n,t,o,a){var s={error:function(e,n,t){alert("Could not contact server ".concat(__apiURL))},type:"POST"};(0,r.send)("token-auth/",{username:e,password:n},s,(function(e){e&&e.token&&(__currentToken=e.token,(0,r.ajaxSetup)(),o(e))}),a,!0,!0)},createSession:function(n,t,o){(0,r.send)("security/createSession",{companyId:n,appVersion:__appVersion},{type:"POST"},(function(n){e(n,t)}),o)},getUserCompanies:function(e,n,t){(0,r.send)("security/getUserCompanies",{user:e,password:n},null,(function(e){t(e)}))},getUserCompaniesFromUserId:function(e,n){(0,r.send)("security/GetUserCompaniesFromUserId/?userId=".concat(e),null,null,(function(e){n(e)}))},logout:function(e){(0,r.send)("security/logout/",null,{dataType:"text"},(function(n){null!=e&&e(n)}))},getAllSessions:function(e){(0,r.send)("security/getAllSessions/",null,null,e,null,!0)},getMySessions:function(e){(0,r.send)("security/getMySessions/",null,null,e,null,!0)},getAllProcess:function(e){(0,r.send)("security/getAllProcess",null,null,e)},createFromToken:function(e,n,t){__currentToken=e,__currentSession={},(0,s.setProcessDictionary)([]),(0,r.ajaxSetup)(),(0,s.setLanguageDictionary)({}),n()},useExternalLink:function(e,n){(0,r.send)("security/useExternalLink/?guid=".concat(e),null,null,(function(e,o){200===o.status?(null!==e.session.companySettingFile&&""!==e.session.companySettingFile&&t.e(42).then((function(){var n=[t(702)("./".concat(e.session.companySettingFile))];(function(){Promise.resolve().then((function(){t(222)})).catch(t.oe)}).apply(null,n)})).catch(t.oe),n(e,o)):n(e,o)}))},killSessionByKey:function(e,n){(0,r.send)("security/killSessionByKey/",{session_key:e},{type:"GET",dataType:"text"},n)},createNewSession:function(n,t){(0,r.send)("security/createNewSession/",null,null,(function(t){e(t,n)}))},requireLogoutSessionByToken:function(e,n){(0,r.send)("security/requireLogout/",{session_key:e},{type:"GET",dataType:"text"},n)},ssoTest:function(){(0,r.send)("security/ssoTest",null,null,(function(e){console.log(e)}))},ssoCheckUser:function(e,n){(0,r.send)("security/SSOCheckUser/",null,null,e,n)},loginas:function(n,t,o,a,s){var i={error:function(e,n,t){alert("Could not contact server ".concat(__apiURL))}};(0,r.send)("security/loginas",{userId:n,token:t,companyId:o},i,(function(n){e(n,a)}))},loginFromToken:function(n,t,o){var a={error:function(e,n,t){alert("Could not contact server ".concat(__apiURL))}};(0,r.send)("security/loginFromToken",{token:n},a,(function(n){e(n,t)}))}})}.apply(n,[]))||(e.exports=a)}).call(this,t(219))}}]);