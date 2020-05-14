/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[279,18,59,300],{1309:function(t,e,n){"use strict";(function(o,s){var r,i,a=n(18);r=[n(816),n(2093),n(685)],void 0===(i=function(t,e,n){return o.View.extend({el:s("#main"),currentObjImport:void 0,render:function(){var t=this,n=e();this.$el.append(n),s("#importDashboardModal").on("hidden.bs.modal",function(){s("#importDashboardModal").off("hidden.bs.modal"),s("#importDashboardModal").remove(),t.currentObjImport=null}).modal("show"),s("#importDashboardModal").css("z-index","4000"),(0,a.postRender)(s("#importDashboardModal")),setTimeout(function(){t.addHandlers(s("#importDashboardModal"))},200)},addHandlers:function(t){var e=this;t.find(".fileSelector").on("change",function(n){var o=n.target.files;if(o.length>0){var s=o[0];if("json"==s.name.split(".").pop().toLowerCase()){var r=new FileReader;r.onload=function(n){var o=r.result;e.loadList(t,o)},r.readAsText(s)}else(0,a.showMessage)((0,a.translate)("incorrect_extension_file"),void 0,"error")}}),t.find(".btnImport").on("click",function(){s(this).prop("disabled","disabled"),t.find(".entry-data select, .entry-data input").prop("disabled","disabled"),t.find(".wait").show(),t.find(".progress").show(),e.importDashboard(t)}),t.find(".btnClose").on("click",function(){s("#importDashboardModal").modal("hide")}),t.find(".filterText1").on("keyup",function(){e.filterItems(t)})},filterItems:function(t){var e=t.find(".filterlist").jstree(!0);if(e){var n=t.find("input.filterText1").val().toLowerCase();e.search(n)}},loadList:function(t,e){if(t.find(".fileSelector").parent().hide(),t.find(".pivotFilter").show(),t.find(".generator").show(),!(0,a.isValidJsonString)(e))return(new n).show({title:"Import Error",text:"Invalid JSON format"}),void s("#importDashboardModal").modal("hide");var o=JSON.parse(e);if(o.dashboards&&o.dashboards.some(function(t){return t.itemType})){var r=o.dashboards.filter(function(t){return 1==t.itemType}).map(function(t){return{id:t.userDashboardId,parent_id:t.parentId,name:t.name,order:t.pos,reports:[],dashboards:[]}}).sort(function(t,e){return t.id<e.id}),i=o.dashboards.filter(function(t){return 2==t.itemType}).map(function(t){return{id:t.dashboardId,report_id:t.parentId,definition:JSON.parse(t.dashboard.definition),name:t.dashboard.name,order:t.pos,node:t.dashboard.node,styles:t.dashboard.styleLibraries}}).sort(function(t,e){return t.id<e.id}),l=[];i.forEach(function(t){if(t.report_id){var e=r.find(function(e){return e.id===t.report_id});e&&(e.dashboards.push(t),l.push(t.id))}}),i=i.filter(function(t){return!l.includes(t.id)}),l=[],r.forEach(function(t){if(t.parent_id){var e=r.find(function(e){return e.id===t.parent_id});e&&(e.reports.push(t),l.push(t.id))}}),r=r.filter(function(t){return!l.includes(t.id)});var d=o.styles.map(function(t){return{id:t.styleLibraryId,name:t.name,definition:JSON.parse(t.definition),style_type:t.libraryType}});o={reports:r,dashboards:i,styles:d}}var c=t.find(".filterlist ul").hide(),u=function(t){t.dashboards.forEach(function(e){s("<li>".concat(e.name,"<ul></ul></li>")).attr("udid",e.id).attr("isparent","0").attr("data_type","dashboard").appendTo(s("li[udid='".concat(t.id,"'] > ul:first-child")))})};o&&(this.currentObjImport=o,o.reports&&o.reports.length>0&&o.reports.forEach(function(t){s("<li>".concat(t.name,"<ul></ul></li>")).attr("udid",t.id).attr("isparent","1").attr("data_type","report").appendTo(c),t.reports&&t.reports.length>0&&function t(e){e.reports.forEach(function(n){s("<li>".concat(n.name,"<ul></ul></li>")).attr("udid",n.id).attr("isparent","0").attr("data_type","report").appendTo(s("li[udid='".concat(e.id,"'] > ul:first-child"))),n.reports&&n.reports.length>0&&t(n),n.dashboards&&n.dashboards.length>0&&u(n)})}(t),t.dashboards&&t.dashboards.length>0&&u(t)}),o.dashboards&&o.dashboards.length>0&&o.dashboards.forEach(function(t){s("<li>"+t.name+"</li>").attr("udid",t.id).attr("data_type","dashboard").appendTo(c)}),c.show(),c.closest(".filterlist").jstree({animation:0,core:{multiple:!0,expand_selected_onload:!1,themes:{icons:!1}},checkbox:{keep_selected_style:!1},search:{case_insensitive:!0,show_only_matches:!0},plugins:["checkbox","search"]}))},importDashboard:function(e){var n=e.find(".filterlist").jstree(!0);if(n){var o=n.get_selected(!0),r={dashboards:[],reports:[],styles:this.currentObjImport.styles};if(o&&o.length>0)if(this.currentObjImport.dashboards&&(r.dashboards=this.currentObjImport.dashboards.filter(function(t){return o.filter(function(t){return"dashboard"===t.li_attr.data_type}).map(function(t){return parseInt(t.li_attr.udid,10)}).includes(t.id)})),this.currentObjImport.reports&&(r.reports=this.currentObjImport.reports.filter(function(t){return o.filter(function(t){return"report"===t.li_attr.data_type}).map(function(t){return parseInt(t.li_attr.udid,10)}).includes(t.id)})),r.reports.length>0||r.dashboards.length>0)(new t).importDashboards(r,function(t){e.find(".wait").hide(),e.find(".progress").hide(),e.modal("hide"),(0,a.showMessage)((0,a.translate)("dashboards_created")," "),s("#report-manager").trigger("fullRefresh")})}}})}.apply(e,r))||(t.exports=i)}).call(this,n(218),n(1))},2093:function(t,e,n){var o=n(690);function s(t){return t&&(t.__esModule?t.default:t)}t.exports=(o.default||o).template({compiler:[8,">= 4.3.0"],main:function(t,e,o,r,i){var a=null!=e?e:t.nullContext||{},l=t.escapeExpression;return'<div id="importDashboardModal" class="modal fade scenario-manager generalExportView" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n    <div class="modal-dialog">\n\n        <div class="modal-content">\n            <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n                <h3>'+l(s(n(688)).call(a,"import_dashboards",{name:"L",hash:{},data:i,loc:{start:{line:7,column:20},end:{line:7,column:45}}}))+'</h3>\n            </div>\n\n            <div class="modal-body">\n\n                <div class="col-sm-12 " >\n                    <input type="file" name="fileToImportDashboard" class="form-control fileSelector" style="height:40px;">\n                </div>\n\n                <div class="col-sm-12 pivotFilter filterview pivotView nodisplay" >\n\n                    <label>'+l(s(n(688)).call(a,"select_dashboards_to_import",{name:"L",hash:{},data:i,loc:{start:{line:18,column:27},end:{line:18,column:62}}}))+'</label>\n\n\n                    <input class="filterText1 form-control " type="text" autofocus placeholder="Search..." >\n\n\n                    <div class="filterlist ">\n                        <ul>\n\n                        </ul>\n                    </div>\n\n                    <br/>\n\n                </div>\n\n\n                <div class="clearfix"></div>\n\n                  <div class="generator nodisplay">\n\n                    <button class="btn btn-primary btn-small btnImport">'+l(s(n(688)).call(a,"import_dashboards",{name:"L",hash:{},data:i,loc:{start:{line:39,column:72},end:{line:39,column:97}}}))+'</button>\n\n                      <span class="wait export-message nodisplay">'+l(s(n(688)).call(a,"please_wait",{name:"L",hash:{},data:i,loc:{start:{line:41,column:66},end:{line:41,column:85}}}))+'</span>\n\n                    <div class="progress progress-striped active nodisplay">\n                        <div class="progress-bar" style="width: 100%;">\n                        </div>\n                    </div>\n                  </div>\n\n                <div class="controls">\n                    <button class="btn btn-small btnClose ">'+l(s(n(688)).call(a,"close",{name:"L",hash:{},data:i,loc:{start:{line:50,column:60},end:{line:50,column:73}}}))+"</button>\n                </div>\n            </div>\n\n\n        </div>\n    </div>\n</div>\n"},useData:!0})},685:function(t,e,n){"use strict";(function(o){var s,r,i=n(18);s=[n(770)],void 0===(r=function(t){return o.Controller.extend({name:"showNotify",currentProgressBar:void 0,show:function(e){var n=e.title,o=e.text,s=e.endpoint,r=e.notifyType,a=e.timeOut,l=e.tapToDismiss,d=e.buttons,c=e.showProgressBar,u=e.showFooter,p=e.callback,h=e.progressBar,f=void 0===h?null:h;if(f&&this.currentProgressBar&&this.currentProgressBar.length>0&&this.currentProgressBar.is(":visible"))return this.currentProgressBar.find(".toast-title").text(n),this.currentProgressBar.find(".toast-text").text(o),this.currentProgressBar.find(".progress-bar").css("width","".concat(f,"%")),void(f>=100&&(this.currentProgressBar.find(".progress").removeClass("active"),this.currentProgressBar.find('button[data-code="cancel"]').text((0,i.translate)("close")),this.currentProgressBar=void 0));var m=new t({title:n,text:o,endpoint:s,notifyType:r,timeOut:a,tapToDismiss:l,buttons:d,showProgressBar:c,showFooter:u,callback:p,progressBar:f}).render();f&&(this.currentProgressBar=m)}})}.apply(e,s))||(t.exports=r)}).call(this,n(694))},741:function(t,e,n){var o,s;n(135),o=[n(1)],void 0===(s=function(t){return function(){function e(e,n){return e||(e=i()),(l=t("#"+e.containerId)).length?l:(n&&(l=function(e){return(l=t("<div/>").attr("id",e.containerId).addClass(e.positionClass).attr("aria-live","polite").attr("role","alert")).appendTo(t(e.target)),l}(e)),l)}function n(e){for(var n=l.children(),s=n.length-1;s>=0;s--)o(t(n[s]),e)}function o(e,n){return!(!e||0!==t(":focus",e).length||(e[n.hideMethod]({duration:n.hideDuration,easing:n.hideEasing,complete:function(){a(e)}}),0))}function s(t){d&&d(t)}function r(n){function o(e){return!t(":focus",h).length||e?(clearTimeout(b.intervalId),h[r.hideMethod]({duration:r.hideDuration,easing:r.hideEasing,complete:function(){a(h),r.onHidden&&"hidden"!==y.state&&r.onHidden(),y.state="hidden",y.endTime=new Date,s(y)}})):void 0}var r=i(),d=n.iconClass||r.iconClass;if(void 0!==n.optionsOverride&&(r=t.extend(r,n.optionsOverride),d=n.optionsOverride.iconClass||d),r.preventDuplicates){if(n.message===c)return;c=n.message}u++,l=e(r,!0);var p=null,h=t("<div/>"),f=t("<div/>"),m=t("<div/>"),g=t("<div/>"),v=t(r.closeHtml),b={intervalId:null,hideEta:null,maxHideTime:null},y={toastId:u,state:"visible",startTime:new Date,options:r,map:n};return n.iconClass&&h.addClass(r.toastClass).addClass(d),n.title&&(f.append(n.title).addClass(r.titleClass),h.append(f)),n.message&&(m.append(n.message).addClass(r.messageClass),h.append(m)),r.closeButton&&(v.addClass("toast-close-button").attr("role","button"),h.prepend(v)),r.progressBar&&(g.addClass("toast-progress"),h.prepend(g)),h.hide(),r.newestOnTop?l.prepend(h):l.append(h),h[r.showMethod]({duration:r.showDuration,easing:r.showEasing,complete:r.onShown}),r.timeOut>0&&(p=setTimeout(o,r.timeOut),b.maxHideTime=parseFloat(r.timeOut),b.hideEta=(new Date).getTime()+b.maxHideTime,r.progressBar&&(b.intervalId=setInterval(function(){var t=(b.hideEta-(new Date).getTime())/b.maxHideTime*100;g.width(t+"%")},10))),h.hover(function(){clearTimeout(p),b.hideEta=0,h.stop(!0,!0)[r.showMethod]({duration:r.showDuration,easing:r.showEasing})},function(){(r.timeOut>0||r.extendedTimeOut>0)&&(p=setTimeout(o,r.extendedTimeOut),b.maxHideTime=parseFloat(r.extendedTimeOut),b.hideEta=(new Date).getTime()+b.maxHideTime)}),!r.onclick&&r.tapToDismiss&&h.click(o),r.closeButton&&v&&v.click(function(t){t.stopPropagation?t.stopPropagation():void 0!==t.cancelBubble&&!0!==t.cancelBubble&&(t.cancelBubble=!0),o(!0)}),r.onclick&&h.click(function(){r.onclick(),o()}),s(y),r.debug&&console&&console.log(y),h}function i(){return t.extend({},{tapToDismiss:!0,toastClass:"toast",containerId:"toast-container",debug:!1,showMethod:"fadeIn",showDuration:300,showEasing:"swing",onShown:void 0,hideMethod:"fadeOut",hideDuration:1e3,hideEasing:"swing",onHidden:void 0,extendedTimeOut:1e3,iconClasses:{error:"toast-error",info:"toast-info",success:"toast-success",warning:"toast-warning"},iconClass:"toast-info",positionClass:"toast-top-right",timeOut:5e3,titleClass:"toast-title",messageClass:"toast-message",target:"body",closeHtml:'<button type="button">&times;</button>',newestOnTop:!0,preventDuplicates:!1,progressBar:!1},h.options)}function a(t){l||(l=e()),t.is(":visible")||(t.remove(),t=null,0===l.children().length&&(l.remove(),c=void 0))}var l,d,c,u=0,p={error:"error",info:"info",success:"success",warning:"warning"},h={clear:function(t){var s=i();l||e(s),o(t,s)||n(s)},remove:function(n){var o=i();return l||e(o),n&&0===t(":focus",n).length?void a(n):void(l.children().length&&l.remove())},error:function(t,e,n){return r({type:p.error,iconClass:i().iconClasses.error,message:t,optionsOverride:n,title:e})},getContainer:e,info:function(t,e,n){return r({type:p.info,iconClass:i().iconClasses.info,message:t,optionsOverride:n,title:e})},options:{},subscribe:function(t){d=t},success:function(t,e,n){return r({type:p.success,iconClass:i().iconClasses.success,message:t,optionsOverride:n,title:e})},version:"2.1.0",warning:function(t,e,n){return r({type:p.warning,iconClass:i().iconClasses.warning,message:t,optionsOverride:n,title:e})}};return h}()}.apply(e,o))||(t.exports=s)},770:function(t,e,n){"use strict";(function(o,s){var r,i,a=function(t){return t&&t.__esModule?t:{default:t}}(n(741));r=[n(771)],void 0===(i=function(t){return o.View.extend({el:s("#main"),currentProgressBar:void 0,defaults:{notifyType:"info",timeOut:3e3},initialize:function(){this.options=s.extend({},this.defaults,this.options)},render:function(){(this.options.buttons||this.options.progressBar)&&(this.options.showFooter=!0,this.options.progressBar&&(this.options.showProgressBar=!0)),a.default.options={closeButton:!0,debug:!1,newestOnTop:!1,progressBar:!1,positionClass:"toast-top-right",preventDuplicates:!1,onclick:null,showDuration:"300",hideDuration:"1000",timeOut:isNaN(parseInt(this.options.timeOut))?__currentSession.notificationTimeOut:this.options.timeOut,extendedTimeOut:0,showEasing:"swing",hideEasing:"linear",showMethod:"fadeIn",hideMethod:"fadeOut",tapToDismiss:this.options.tapToDismiss};var e=t(this.options),n=a.default[this.options.notifyType](e,this.options.title);this.options.notifyClass&&n.addClass(this.options.notifyClass);var o=this;return n.find(".footer-area button").click(function(){var t=!0;return o.options.callback&&!1===o.options.callback.call(this,s(this).attr("data-code"),n)&&(t=!1),t&&n.find(".toast-close-button").click(),!1}),n}})}.apply(e,r))||(t.exports=i)}).call(this,n(218),n(1))},771:function(t,e,n){var o=n(690);t.exports=(o.default||o).template({1:function(t,e,n,o,s){var r,i=null!=e?e:t.nullContext||{};return'<div class="footer-area">\n'+(null!=(r=n.if.call(i,null!=e?e.showProgressBar:e,{name:"if",hash:{},fn:t.program(2,s,0),inverse:t.noop,data:s,loc:{start:{line:11,column:2},end:{line:15,column:9}}}))?r:"")+"\n"+(null!=(r=n.each.call(i,null!=e?e.buttons:e,{name:"each",hash:{},fn:t.program(4,s,0),inverse:t.noop,data:s,loc:{start:{line:17,column:2},end:{line:19,column:11}}}))?r:"")+"\n</div>\n"},2:function(t,e,n,o,s){var r;return'  <div class="progress progress-striped active">\n    <div class="progress-bar progress-bar-warning" style="width: '+t.escapeExpression("function"==typeof(r=null!=(r=n.progressBar||(null!=e?e.progressBar:e))?r:t.hooks.helperMissing)?r.call(null!=e?e:t.nullContext||{},{name:"progressBar",hash:{},data:s,loc:{start:{line:13,column:65},end:{line:13,column:80}}}):r)+'%"></div>\n  </div>\n'},4:function(t,e,n,o,s){var r,i=null!=e?e:t.nullContext||{},a=t.hooks.helperMissing,l=t.escapeExpression;return'  <button class="btn btn-mini btn-'+l("function"==typeof(r=null!=(r=n.css||(null!=e?e.css:e))?r:a)?r.call(i,{name:"css",hash:{},data:s,loc:{start:{line:18,column:34},end:{line:18,column:41}}}):r)+'" data-code="'+l("function"==typeof(r=null!=(r=n.code||(null!=e?e.code:e))?r:a)?r.call(i,{name:"code",hash:{},data:s,loc:{start:{line:18,column:54},end:{line:18,column:62}}}):r)+'">'+l("function"==typeof(r=null!=(r=n.title||(null!=e?e.title:e))?r:a)?r.call(i,{name:"title",hash:{},data:s,loc:{start:{line:18,column:64},end:{line:18,column:73}}}):r)+"</button>\n"},compiler:[8,">= 4.3.0"],main:function(t,e,n,o,s){var r,i,a=null!=e?e:t.nullContext||{},l=t.hooks.helperMissing;return'<span class="toast-text">\n  <div>\n    '+(null!=(r="function"==typeof(i=null!=(i=n.text||(null!=e?e.text:e))?i:l)?i.call(a,{name:"text",hash:{},data:s,loc:{start:{line:3,column:4},end:{line:3,column:14}}}):i)?r:"")+"\n  </div>\n  <div>\n    "+(null!=(r="function"==typeof(i=null!=(i=n.endpoint||(null!=e?e.endpoint:e))?i:l)?i.call(a,{name:"endpoint",hash:{},data:s,loc:{start:{line:6,column:4},end:{line:6,column:18}}}):i)?r:"")+"\n  </div>\n</span>\n"+(null!=(r=n.if.call(a,null!=e?e.showFooter:e,{name:"if",hash:{},fn:t.program(1,s,0),inverse:t.noop,data:s,loc:{start:{line:9,column:0},end:{line:22,column:7}}}))?r:"")},useData:!0})},816:function(t,e,n){"use strict";(function(o){var s,r=n(693);void 0===(s=function(){return o.Model.extend({url:"inputModule",defaults:{formsViewList:[]},search:function(t,e){(0,r.send)("reportManager/search/?text=".concat(t),null,{type:"GET"},e)},getMyReports:function(t,e){(0,r.send)("reportManager/myReports/?parent=".concat(t),null,{type:"GET"},e)},getFavsReports:function(t,e){(0,r.send)("reportManager/myReports/?favs=true",null,{type:"GET"},e)},getReportsSharedWithMe:function(t,e){(0,r.send)("reportManager/sharedWithMe/?parent=".concat(t),null,{type:"GET"},e)},getMySharedReports:function(t,e){(0,r.send)("reportManager/mySharedReports/",null,{type:"GET"},e)},getRecentsReports:function(t,e){(0,r.send)("reportManager/recents/?parent=".concat(t),null,{type:"GET"},e)},exportDashboards:function(t,e){var o=new XMLHttpRequest;o.responseType="arraybuffer",o.open("PUT","".concat(__apiURL,"/reportManager/exportItems/"),!0),o.setRequestHeader("Authorization","Token ".concat(__currentToken)),o.setRequestHeader("session-key",__currentSession?__currentSession.session_key:""),o.setRequestHeader("Content-type","application/json"),o.onreadystatechange=function(t){var o=t.currentTarget;o.readyState==o.DONE&&(200==o.status?e(o):n.e(18).then(function(){var t=[n(685)];(function(t){(new t).show({title:"ERROR!",text:o.response,notifyType:"error"})}).apply(null,t)}).catch(n.oe))},o.send(JSON.stringify(t))},exportItemsAndPublish:function(t,e,n,o,s,i,a){(0,r.send)("reportManager/exportItemsAndPublish/",JSON.stringify({username:t,uuid:e,model_folder:n,model_id:o,dashboard_ids:s,report_ids:i}),{type:"PUT",contentType:"application/json;charset=utf-8"},a)},importDashboards:function(t,e){(0,r.send)("reportManager/importItems/",JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8"},e)},create:function(t,e){(0,r.send)("reportManager/",t,{type:"POST"},function(t){void 0!=e&&e(t)})},createReport:function(t,e){(0,r.send)("reportManager/",t,{type:"POST"},function(t){void 0!=e&&e(t)})},dropOnReport:function(t,e){(0,r.send)("reportManager/dropOnReport/",JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8"},e)},updateOrder:function(t){(0,r.send)("reportManager/changeOrder/",JSON.stringify({values:t}),{type:"PUT",contentType:"application/json;charset=utf-8"},function(t){})},setAsFav:function(t,e,n){(0,r.send)("reportManager/setAsFav/",JSON.stringify({report_ids:t.report_ids,dashboard_ids:t.dashboard_ids,is_fav:e}),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},n)},updateName:function(t,e,n){(0,r.send)("reportManager/".concat(t,"/"),{name:e},{type:"PUT",dataType:"text"},function(t){void 0!=n&&n(t)})},deleteItems:function(t,e){(0,r.send)("reportManager/bulkDelete/",JSON.stringify({values:t}),{type:"DELETE",contentType:"application/json;charset=utf-8"},function(t){void 0!=e&&e(t)})},createTempId:function(){return"tmp-".concat(parseInt(5e5*Math.random()))},copyToMyReports:function(t,e){(0,r.send)("reportManager/copyToMyReports/",JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},function(t){void 0!=e&&e(t)})},duplicateItems:function(t,e){(0,r.send)("reportManager/duplicateItems/",JSON.stringify(t),{type:"PUT",contentType:"application/json;charset=utf-8",dataType:"text"},function(t){e&&e(t)})}})}.apply(e,[]))||(t.exports=s)}).call(this,n(218))}}]);