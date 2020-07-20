/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[122,7],{1295:function(n,t,e){"use strict";var a=e(18);n.exports=function(n){return(0,a.formatDate)(n)}},1639:function(n,t,e){"use strict";(function(a,r){var s,o,l=e(18),i=e(742);function u(n,t,e,a,r,s,o){try{var l=n[s](o),i=l.value}catch(n){return void e(n)}l.done?t(i):Promise.resolve(i).then(a,r)}s=[e(663),e(2615)],void 0===(o=function(n,t){var e,s,o=this;return a.View.extend({el:r("#main"),render:(e=regeneratorRuntime.mark((function e(a){var r;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return o.fromDashboard=!!a.fromDashboard,e.next=3,(0,i.listTaskItemHistoryById)(a.id);case 3:a.history=e.sent,r=t(a),(new n).show({title:a.title,html:r,modalClass:"mediumModal",buttons:[{title:(0,l.translate)("close"),code:"close"}],callback:function(n,t){return t.modal("hide"),!1},onLoad:function(n){(0,l.postRender)(n)},onClose:function(n){}});case 7:case"end":return e.stop()}}),e,this)})),s=function(){var n=this,t=arguments;return new Promise((function(a,r){var s=e.apply(n,t);function o(n){u(s,a,r,o,l,"next",n)}function l(n){u(s,a,r,o,l,"throw",n)}o(void 0)}))},function(n){return s.apply(this,arguments)})})}.apply(t,s))||(n.exports=o)}).call(this,e(219),e(1))},2615:function(n,t,e){var a=e(670);function r(n){return n&&(n.__esModule?n.default:n)}n.exports=(a.default||a).template({1:function(n,t,a,s,o,l,i){var u,c=null!=t?t:n.nullContext||{},p=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'          <li>\n            <div class="timeline-content">\n              <div class="left">\n                <div class="date">'+n.escapeExpression(r(e(1295)).call(c,null!=t?p(t,"created_at"):t,{name:"formatDate",hash:{},data:o,loc:{start:{line:10,column:34},end:{line:10,column:59}}}))+"</div>\n              </div>\n\n"+(null!=(u=r(e(669)).call(c,null!=t?p(t,"action"):t,"==","create",{name:"ifCond",hash:{},fn:n.program(2,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:13,column:14},end:{line:21,column:25}}}))?u:"")+"\n"+(null!=(u=r(e(669)).call(c,null!=t?p(t,"action"):t,"==","update",{name:"ifCond",hash:{},fn:n.program(4,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:23,column:14},end:{line:72,column:25}}}))?u:"")+"\n"+(null!=(u=p(a,"if").call(c,null!=(u=null!=t?p(t,"extra_data"):t)?p(u,"comments"):u,{name:"if",hash:{},fn:n.program(15,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:74,column:14},end:{line:84,column:21}}}))?u:"")+'            </div>\n            <div class="line"></div>\n          </li>\n'},2:function(n,t,a,s,o){var l,i=n.lambda,u=n.escapeExpression,c=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'              <div class="activity">\n                <div class="user">\n                  <span class="user">'+u(i(null!=(l=null!=t?c(t,"extra_data"):t)?c(l,"performer"):l,t))+"</span>\n                  <span>"+u(r(e(668)).call(null!=t?t:n.nullContext||{},"_wfTaskItemHistoryCreated",{name:"L",hash:{},data:o,loc:{start:{line:17,column:24},end:{line:17,column:57}}}))+'</span>\n                  <span class="user">'+u(i(null!=(l=null!=t?c(t,"extra_data"):t)?c(l,"responsible"):l,t))+"</span>\n                </div>\n              </div>\n"},4:function(n,t,e,a,r,s,o){var l,i=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return null!=(l=i(e,"if").call(null!=t?t:n.nullContext||{},null!=(l=null!=t?i(t,"extra_data"):t)?i(l,"changes"):l,{name:"if",hash:{},fn:n.program(5,r,0,s,o),inverse:n.noop,data:r,loc:{start:{line:24,column:14},end:{line:71,column:21}}}))?l:""},5:function(n,t,e,a,r,s,o){var l,i=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return null!=(l=i(e,"each").call(null!=t?t:n.nullContext||{},null!=(l=null!=t?i(t,"extra_data"):t)?i(l,"changes"):l,{name:"each",hash:{},fn:n.program(6,r,0,s,o),inverse:n.noop,data:r,loc:{start:{line:25,column:14},end:{line:70,column:23}}}))?l:""},6:function(n,t,a,s,o,l,i){var u,c=null!=t?t:n.nullContext||{},p=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return(null!=(u=r(e(669)).call(c,null!=t?p(t,"field"):t,"==","start",{name:"ifCond",hash:{},fn:n.program(7,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:26,column:14},end:{line:36,column:25}}}))?u:"")+(null!=(u=r(e(669)).call(c,null!=t?p(t,"field"):t,"==","end",{name:"ifCond",hash:{},fn:n.program(9,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:37,column:14},end:{line:47,column:25}}}))?u:"")+(null!=(u=r(e(669)).call(c,null!=t?p(t,"field"):t,"==","percentage",{name:"ifCond",hash:{},fn:n.program(11,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:48,column:14},end:{line:58,column:25}}}))?u:"")+(null!=(u=r(e(669)).call(c,null!=t?p(t,"field"):t,"==","status",{name:"ifCond",hash:{},fn:n.program(13,o,0,l,i),inverse:n.noop,data:o,loc:{start:{line:59,column:14},end:{line:69,column:25}}}))?u:"")},7:function(n,t,a,s,o,l,i){var u,c=n.lambda,p=n.escapeExpression,d=null!=t?t:n.nullContext||{},f=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'              <div class="activity">\n                <div class="user">\n                  <span class="user">'+p(c(null!=(u=null!=i[1]?f(i[1],"extra_data"):i[1])?f(u,"performer"):u,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryUpdateStart",{name:"L",hash:{},data:o,loc:{start:{line:30,column:24},end:{line:30,column:61}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"old_value"):t,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryTo",{name:"L",hash:{},data:o,loc:{start:{line:32,column:24},end:{line:32,column:52}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"new_value"):t,t))+"</span>\n                </div>\n              </div>\n"},9:function(n,t,a,s,o,l,i){var u,c=n.lambda,p=n.escapeExpression,d=null!=t?t:n.nullContext||{},f=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'              <div class="activity">\n                <div class="user">\n                  <span class="user">'+p(c(null!=(u=null!=i[1]?f(i[1],"extra_data"):i[1])?f(u,"performer"):u,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryUpdateEnd",{name:"L",hash:{},data:o,loc:{start:{line:41,column:24},end:{line:41,column:59}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"old_value"):t,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryTo",{name:"L",hash:{},data:o,loc:{start:{line:43,column:24},end:{line:43,column:52}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"new_value"):t,t))+"</span>\n                </div>\n              </div>\n"},11:function(n,t,a,s,o,l,i){var u,c=n.lambda,p=n.escapeExpression,d=null!=t?t:n.nullContext||{},f=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'              <div class="activity">\n                <div class="user">\n                  <span class="user">'+p(c(null!=(u=null!=i[1]?f(i[1],"extra_data"):i[1])?f(u,"performer"):u,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryUpdatePercentage",{name:"L",hash:{},data:o,loc:{start:{line:52,column:24},end:{line:52,column:66}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"old_value"):t,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryTo",{name:"L",hash:{},data:o,loc:{start:{line:54,column:24},end:{line:54,column:52}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"new_value"):t,t))+"</span>\n                </div>\n              </div>\n"},13:function(n,t,a,s,o,l,i){var u,c=n.lambda,p=n.escapeExpression,d=null!=t?t:n.nullContext||{},f=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'              <div class="activity">\n                <div class="user">\n                  <span class="user">'+p(c(null!=(u=null!=i[1]?f(i[1],"extra_data"):i[1])?f(u,"performer"):u,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryUpdateStatus",{name:"L",hash:{},data:o,loc:{start:{line:63,column:24},end:{line:63,column:62}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"old_value"):t,t))+"</span>\n                  <span>"+p(r(e(668)).call(d,"_wfTaskItemHistoryTo",{name:"L",hash:{},data:o,loc:{start:{line:65,column:24},end:{line:65,column:52}}}))+'</span>\n                  <span class="user">'+p(c(null!=t?f(t,"new_value"):t,t))+"</span>\n                </div>\n              </div>\n"},15:function(n,t,a,s,o){var l,i=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return null!=(l=r(e(669)).call(null!=t?t:n.nullContext||{},null!=(l=null!=t?i(t,"extra_data"):t)?i(l,"comments"):l,"!=","",{name:"ifCond",hash:{},fn:n.program(16,o,0),inverse:n.noop,data:o,loc:{start:{line:75,column:14},end:{line:83,column:25}}}))?l:""},16:function(n,t,a,s,o){var l,i=n.lambda,u=n.escapeExpression,c=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'              <div class="activity">\n                <div class="user">\n                  <span class="user">'+u(i(null!=(l=null!=t?c(t,"extra_data"):t)?c(l,"performer"):l,t))+"</span>\n                  <span>"+u(r(e(668)).call(null!=t?t:n.nullContext||{},"_wfTaskItemHistoryComment",{name:"L",hash:{},data:o,loc:{start:{line:79,column:24},end:{line:79,column:57}}}))+'</span>\n                  <span class="user">'+u(i(null!=(l=null!=t?c(t,"extra_data"):t)?c(l,"comments"):l,t))+"</span>\n                </div>\n              </div>\n"},compiler:[8,">= 4.3.0"],main:function(n,t,e,a,r,s,o){var l,i=n.lookupProperty||function(n,t){if(Object.prototype.hasOwnProperty.call(n,t))return n[t]};return'<div class="box">\n  <div class="box-content nopadding">\n    <div class="tab-content padding tab-content-inline tab-content-bottom">\n      <div class="ganttTaskEditorHistory tab-pane active" id="taskItemHistoryModal">\n        <ul class="timeline">\n'+(null!=(l=i(e,"each").call(null!=t?t:n.nullContext||{},null!=t?i(t,"history"):t,{name:"each",hash:{},fn:n.program(1,r,0,s,o),inverse:n.noop,data:r,loc:{start:{line:6,column:10},end:{line:88,column:19}}}))?l:"")+"        </ul>\n      </div>\n    </div>\n  </div>\n</div>"},useData:!0,useDepths:!0})},663:function(n,t,e){"use strict";(function(a){var r;void 0===(r=function(){return a.Controller.extend({name:"showModal",show:function(n){Promise.all([e.e(2),e.e(228)]).then((function(){var t=[e(686)];(function(t){(new t).render(n)}).apply(null,t)})).catch(e.oe)}})}.apply(t,[]))||(n.exports=r)}).call(this,e(677))},714:function(n,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.requestFile=t.request=void 0;var a=e(18);function r(n,t,e){return t in n?Object.defineProperty(n,t,{value:e,enumerable:!0,configurable:!0,writable:!0}):n[t]=e,n}function s(n,t,e,a,r,s,o){try{var l=n[s](o),i=l.value}catch(n){return void e(n)}l.done?t(i):Promise.resolve(i).then(a,r)}function o(n){return function(){var t=this,e=arguments;return new Promise((function(a,r){var o=n.apply(t,e);function l(n){s(o,a,r,l,i,"next",n)}function i(n){s(o,a,r,l,i,"throw",n)}l(void 0)}))}}var l=__apiURL,i=function(n){if(n&&n.hasError){var t=new Error(n.error);throw t.response=n,t}return n},u=function(n){var t=n.fileName,e=n.response;if(e&&e.hasError){var a=new Error(e.error);throw a.response=e,a}return{fileName:t,response:e}},c=function(n){return n.text().then((function(n){return n?JSON.parse(n):{}}))},p=function(){var n=o(regeneratorRuntime.mark((function n(t){var e,a;return regeneratorRuntime.wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return e=t.headers.get("Content-Disposition").split("=")[1].replace(/['"]/g,""),n.next=3,t.blob().then((function(n){return n}));case 3:return a=n.sent,n.abrupt("return",{fileName:e,response:a});case 5:case"end":return n.stop()}}),n,this)})));return function(t){return n.apply(this,arguments)}}(),d=function(n){if(n.status>=200&&n.status<300)return n;var t=new Error(n.statusText);t.response=n,n.text().then((function(e){throw(0,a.showMessage)("status : ".concat(n.status," <br/> ").concat(n.statusText," <br/> ").concat(e),(0,a.translate)("_request_error_in_fetch"),"error"),t}))},f=function(n,t){var e=__currentToken,a=n,s=n.headers?n.headers:{};if(e&&t.indexOf("/security/login?")<0){var o=new Headers(function(n){for(var t=1;t<arguments.length;t++){var e=null!=arguments[t]?arguments[t]:{},a=Object.keys(e);"function"==typeof Object.getOwnPropertySymbols&&(a=a.concat(Object.getOwnPropertySymbols(e).filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable})))),a.forEach((function(t){r(n,t,e[t])}))}return n}({Authorization:"Token ".concat(__currentToken),"session-key":__currentSession?__currentSession.session_key:""},s));a.headers=o}return a},m=function(){var n=o(regeneratorRuntime.mark((function n(t,e){var a;return regeneratorRuntime.wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return a=f(e,t),n.abrupt("return",fetch("".concat(l).concat(t),a).then(d).then(c).then(i));case 2:case"end":return n.stop()}}),n,this)})));return function(t,e){return n.apply(this,arguments)}}();t.request=m;var h=function(){var n=o(regeneratorRuntime.mark((function n(t,e){var a;return regeneratorRuntime.wrap((function(n){for(;;)switch(n.prev=n.next){case 0:return a=f(e,t),n.abrupt("return",fetch("".concat(l).concat(t),a).then(d).then(p).then(u));case 2:case"end":return n.stop()}}),n,this)})));return function(t,e){return n.apply(this,arguments)}}();t.requestFile=h},742:function(n,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.bulkPartialUpdateTaskItemStatusTransition=t.listPosibleByFromStatusId=t.listTaskItemStatusTransitions=t.deleteTaskItemStatus=t.partialUpdateTaskItemStatus=t.createTaskItemStatus=t.listTaskItemStatuses=t.listTaskItemHistoryById=t.bulkPartialUpdateTaskItem=t.partialUpdateTaskItem=t.deleteTaskGroup=t.partialUpdateTaskGroup=t.createTaskGroup=t.listTaskGroups=t.deleteTask=t.listTasksByGroupsIds=t.listTasksByStatusId=t.listTasks=t.createTask=void 0;var a=e(714);function r(n,t){return function(n){if(Array.isArray(n))return n}(n)||function(n,t){var e=[],a=!0,r=!1,s=void 0;try{for(var o,l=n[Symbol.iterator]();!(a=(o=l.next()).done)&&(e.push(o.value),!t||e.length!==t);a=!0);}catch(n){r=!0,s=n}finally{try{a||null==l.return||l.return()}finally{if(r)throw s}}return e}(n,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}t.createTask=function(n){return(0,a.request)("/wftask/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)})};t.listTasks=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=Object.keys(n).length>0&&Object.entries(n).map((function(n){var t=r(n,2),e=t[0],a=t[1];return"".concat(e,"=").concat(a)})).join("&");return(0,a.request)("/wftask/".concat(t?"?".concat(t):""),{method:"GET"})};t.listTasksByStatusId=function(n){return(0,a.request)("/wftask/list_by_status_id/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id:n})})};t.listTasksByGroupsIds=function(n){return(0,a.request)("/wftask/list_by_groups_ids/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({groups_ids:n})})};t.deleteTask=function(n){return(0,a.request)("/wftask/".concat(n,"/"),{method:"DELETE"})};t.listTaskGroups=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=Object.keys(n).length>0&&Object.entries(n).map((function(n){var t=r(n,2),e=t[0],a=t[1];return"".concat(e,"=").concat(a)})).join("&");return(0,a.request)("/wftaskgroup/".concat(t?"?".concat(t):""),{method:"GET"})};t.createTaskGroup=function(n){return(0,a.request)("/wftaskgroup/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)})};t.partialUpdateTaskGroup=function(n,t){return(0,a.request)("/wftaskgroup/".concat(n,"/"),{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(t)})};t.deleteTaskGroup=function(n){return(0,a.request)("/wftaskgroup/".concat(n,"/"),{method:"DELETE"})};t.partialUpdateTaskItem=function(n,t){return(0,a.request)("/wftaskitem/".concat(n,"/"),{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(t)})};t.bulkPartialUpdateTaskItem=function(n){return(0,a.request)("/wftaskitem/bulk_partial_update/",{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)})};t.listTaskItemHistoryById=function(n){return(0,a.request)("/wftaskitemhistory/list_by_task_item_id/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id:n})})};t.listTaskItemStatuses=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=Object.keys(n).length>0&&Object.entries(n).map((function(n){var t=r(n,2),e=t[0],a=t[1];return"".concat(e,"=").concat(a)})).join("&");return(0,a.request)("/wftaskitemstatus/".concat(t?"?".concat(t):""),{method:"GET"})};t.createTaskItemStatus=function(n){return(0,a.request)("/wftaskitemstatus/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)})};t.partialUpdateTaskItemStatus=function(n,t){return(0,a.request)("/wftaskitemstatus/".concat(n,"/"),{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(t)})};t.deleteTaskItemStatus=function(n){return(0,a.request)("/wftaskitemstatus/".concat(n,"/"),{method:"DELETE"})};t.listTaskItemStatusTransitions=function(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=Object.keys(n).length>0&&Object.entries(n).map((function(n){var t=r(n,2),e=t[0],a=t[1];return"".concat(e,"=").concat(a)})).join("&");return(0,a.request)("/wftaskitemstatustransition/".concat(t?"?".concat(t):""),{method:"GET"})};t.listPosibleByFromStatusId=function(n){return(0,a.request)("/wftaskitemstatustransition/list_posible_by_from_status_id/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)})};t.bulkPartialUpdateTaskItemStatusTransition=function(n){return(0,a.request)("/wftaskitemstatustransition/bulk_partial_update/",{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)})}}}]);