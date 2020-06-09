/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[157,6],{2347:function(e,n,t){"use strict";(function(o,a){var i,c,r=t(18);i=[t(674),t(2348),t(715)],void 0===(c=function(e,n,t){return o.View.extend({el:a("#main"),render:function(o,i,c){var l=n({source:o}),s=new t,d=this,u=i?(0,r.translate)("move_to"):(0,r.translate)("copy_in");a("#tree-container").perfectScrollbar(),(new e).show({title:u,html:l,modalClass:"shortModal",buttons:[{title:(0,r.translate)("yes"),css:"primary",code:"yes"},{title:(0,r.translate)("close"),code:"close"}],callback:function(e,n){if("yes"==e){n.modal("hide");var l=a("#right-column > div.fm-highlight-toolbar > div.pull-left a").not('[disabled="disabled"]');l.attr("disabled","disabled");var s=new t;return i?(0,r.haveAccess)("add_file_public")&&d.isInPublic(d.moveToPath)||!d.isInPublic(d.moveToPath)?s.moveFiles(o,d.moveToPath,(function(){c(d.moveToPath),l.removeAttr("disabled")})):(l.removeAttr("disabled"),(0,r.showMessage)("".concat((0,r.translate)("no_permission_to_perform_action")," - permission: add_file_public"),"Move Files","info")):(0,r.haveAccess)("add_file_public")&&d.isInPublic(d.moveToPath)||!d.isInPublic(d.moveToPath)?s.copyFiles(o,d.moveToPath,(function(){c(d.moveToPath),l.removeAttr("disabled")})):(l.removeAttr("disabled"),(0,r.showMessage)("".concat((0,r.translate)("no_permission_to_perform_action")," - permission: add_file_public"),"Copy Files","info")),!1}},onLoad:function(){setTimeout((function(){a("#main-modal button.btn-primary").focus()}),500),a("#treeMoveTo").jstree({plugins:["wholerow","types","contextmenu","dnd"],types:{default:{icon:"fa fa-folder"},folder:{icon:"fa fa-folder"},shared:{icon:"fa fa-users"},recent:{icon:"fa fa-clock"},favs:{icon:"fa fa-star"},trash:{icon:"fa fa-trash"},file:{icon:"fa fa-file"},myfolder:{icon:"fa fa-user"},public:{icon:"fa fa-globe"},zip:{icon:"fa-file-archive-o"},modelsPath:{icon:"fa fa-cubes"},model:{icon:"fa fa-cube"}},core:{check_callback:!0,themes:{name:"proton",responsive:!0},data:function(e,n){if("#"===e.id)s.getMainFolders((function(e){null!==e&&(e=d.optimizeStructureForTree(e,"tree"),n.call(this,e)),d.openRootNodes(e)}));else{var t=""===e.data.fullPath?"/":e.data.fullPath;s.getFiles(t,(function(e){null!==e&&(e=d.optimizeStructureForTree(e,"tree"),n.call(this,e))}))}}}}).on("changed.jstree",(function(e,n){if(n.node){var t=""===n.node.data.fullPath?"/":n.node.data.fullPath;d.moveToPath=t,s.getFiles(t,(function(e){null!==e&&(e=d.optimizeStructureForTree(e,"list"))}))}}))}})},openRootNodes:function(e){var n=setInterval((function(){if(a("#treeMoveTo .jstree-container-ul li").length===e.length){clearInterval(n);var t=0;a("#treeMoveTo .jstree-container-ul li").each((function(){0===t&&a("#treeMoveTo").jstree("select_node",a(this),!1,!0),a("#treeMoveTo").jstree("open_node",a(this)),t++}))}}),5)},optimizeStructureForTree:function(e,n){var t=[];(0,r.haveAccess)("copy_model_to_my_workspace")||0!==e[0].type||e.splice(0,1);for(var o=0;o<e.length;o++){if(1===e[o].type||0===e[o].type?(e[o].children=!0,e[o].type="folder"):"tree"===n&&t.push(o),0!==e[o].data.specialFolderType)switch(e[o].children=!0,e[o].data.specialFolderType){case 0:e[o].type="folder";break;case 1:e[o].type="myfolder";break;case 2:e[o].type="public";break;case 3:e[o].type="company";break;case 4:e[o].type="modelsPath";break;case 5:e[o].type="shared";break;default:e[o].type="folder"}if(0===e[o].type||2===e[o].type)switch(e[o].data.specialFileType){case 0:e[o].type="file";break;case 1:e[o].type="model";break;case 2:e[o].type="zip";break;default:e[o].type="file"}}if("tree"===n)for(var a=0;a<t.length;a++)e.splice(t[t.length-(a+1)],1);return e},isInPublic:function(e){return e.toLowerCase().indexOf("/public/")>=0||e.toLowerCase().endsWith("/public")}})}.apply(n,i))||(e.exports=c)}).call(this,t(220),t(1))},2348:function(e,n,t){var o=t(681);e.exports=(o.default||o).template({compiler:[8,">= 4.3.0"],main:function(e,n,t,o,a){return'<div class="box">\n    <span>Choose destination for selected element(s)</span>\n\n    <div class="box-content">\n      <div class="row">\n        <div class="col-sm-12">\n\n          \x3c!-- START: Left column --\x3e\n          <div id="tree-container" class="col-sm-12 nopadding" style="overflow: scroll; height: 350px;">\n\n            <div id="treeMoveTo"></div>\n\n          </div>\n          \x3c!-- END: Left column --\x3e\n        </div>\n      </div>\n\n    </div>\n</div>\n'},useData:!0})},674:function(e,n,t){"use strict";(function(o){var a;void 0===(a=function(){return o.Controller.extend({name:"showModal",show:function(e){Promise.all([t.e(2),t.e(227)]).then((function(){var n=[t(697)];(function(n){(new n).render(e)}).apply(null,n)})).catch(t.oe)}})}.apply(n,[]))||(e.exports=a)}).call(this,t(688))},715:function(e,n,t){"use strict";(function(o){var a,i=t(689);void 0===(a=function(){return o.Model.extend({url:"myFileManager",getMainFolders:function(e){(0,i.send)("fileManager/getMainFolders/",null,{type:"GET"},e)},getFiles:function(e,n){(0,i.send)("fileManager/getFiles/?folder=".concat(encodeURIComponent(e)),null,{type:"GET"},n)},createFolder:function(e,n,t){(0,i.send)("fileManager/createFolder/",{folder_path:e,folder_name:n},{type:"POST"},t)},deleteFiles:function(e,n){(0,i.send)("fileManager/deleteFiles/",JSON.stringify({sources:e}),{type:"DELETE",contentType:"application/json",dataType:"text"},n)},renameFiles:function(e,n,t){(0,i.send)("fileManager/renameFile/?source=".concat(encodeURIComponent(e),"&newName=").concat(n),null,{type:"GET"},t)},unzipFile:function(e,n,t){(0,i.send)("fileManager/unzipFile/?source=".concat(e,"&targetFolder=").concat(encodeURIComponent(n)),null,{type:"GET",dataType:"text"},t)},moveFiles:function(e,n,t){var o=e.map((function(e){return"sources=".concat(e)})).join("&");(0,i.send)("fileManager/moveFiles/?".concat(o,"&target=").concat(encodeURIComponent(n)),null,{type:"GET",dataType:"text"},t)},copyToMyWorkspace:function(e,n){(0,i.send)("fileManager/copyToMyWorkspace/?source="+encodeURIComponent(e),null,{type:"GET",dataType:"text"},n)},copyFiles:function(e,n,t){var o=e.map((function(e){return"sources=".concat(e)})).join("&");(0,i.send)("fileManager/copyFiles/?".concat(o,"&target=").concat(encodeURIComponent(n)),null,{type:"GET",dataType:"text"},t)},duplicateFiles:function(e,n){var t=e.map((function(e){return"sources=".concat(e)})).join("&");(0,i.send)("fileManager/duplicateFiles/?".concat(t),null,{type:"GET"},n)},zipFiles:function(e,n){var t=e.map((function(e){return"sources=".concat(e)})).join("&");(0,i.send)("fileManager/zipFiles/?".concat(t),null,{type:"GET",dataType:"text"},n)},downloadFiles:function(e,n){var o=arguments.length>2&&void 0!==arguments[2]?arguments[2]:function(){},a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:function(){},i=arguments.length>4&&void 0!==arguments[4]?arguments[4]:function(){},c=arguments.length>5&&void 0!==arguments[5]?arguments[5]:function(){},r=e.map((function(e){return"sources=".concat(e)})).join("&"),l=new XMLHttpRequest;l.responseType="arraybuffer",l.open("GET","".concat(__apiURL,"/fileManager/download/?").concat(r),!0),l.setRequestHeader("Authorization","Token ".concat(__currentToken)),l.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),l.onloadstart=o,l.onreadystatechange=function(e){var o=e.currentTarget;o.onprogress=a,o.onerror=c,o.onloadend=i,o.readyState==o.DONE&&(200==o.status?n(o):t.e(18).then((function(){var e=[t(676)];(function(e){(new e).show({title:"ERROR!",text:o.response,notifyType:"error"})}).apply(null,e)})).catch(t.oe))},l.send()},getDepartments:function(e){(0,i.send)("departments/by_current_company/",null,{type:"GET"},e)},getDeniedDepartments:function(e,n){(0,i.send)("departments/denied/?folder=".concat(encodeURIComponent(e)),null,{type:"GET"},n)},setDeniedPath:function(e,n){(0,i.send)("departments/deny_items/",JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8"},n)},optimzeTemplates:function(e,n,t){var o=e.map((function(e){return"sources=".concat(e)})).join("&");(0,i.send)("fileManager/optimizeTemplates/?".concat(o),null,{type:"GET",dataType:"text"},n,t)}})}.apply(n,[]))||(e.exports=a)}).call(this,t(220))}}]);