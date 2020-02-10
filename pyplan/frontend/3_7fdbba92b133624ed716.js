/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{699:function(n,e,a){"use strict";(function(t,r){var o,i,s=a(18);o=[a(684),a(762),a(763)],void 0===(i=function(n,e,o){return t.Controller.extend({name:"modelManager",currentModelUri:"",setCurrentUri:function(n){this.currentModelUri=n},open:function(n,e){e&&(this.currentModelUri="_no_model_name_"),this.openSummary(n)},openSummary:function(t){var o=new n,i="",l=this,c=function(n){if(l.currentModelUri=n,o.existsTask(i))o.selectTask(i);else if((0,s.haveAccess)("view_influence_diagram")){var t=new e;t.render(),Promise.resolve().then(function(){var e=[a(219)];(function(e){(new e).openModel(n,function(n){if(t.done(),r("#mainLoading").hide(),n)switch(r("#navigation .modelopened").show(),r("#left .navigation .modelopened").show(),n.onOpenModel){case"openDiagram":case"":i="influence_diagram",o.addSimpleTask(i,(0,s.translate)("model")),Promise.all([a.e(11),a.e(20),a.e(22)]).then(function(){var n=[a(714)];(function(n){(new n).showDiagram()}).apply(null,n)}).catch(a.oe),o.selectTask(i);break;case"openReportManager":a.e(53).then(function(){var n=[a(766)];(function(n){(new n).show()}).apply(null,n)}).catch(a.oe);break;case"openDashboard":a.e(32).then(function(){var e=[a(702)];(function(e){(new e).showDashboard(n.onOpenDashId,null,"",!1,!0,null,null)}).apply(null,e)}).catch(a.oe)}},!1,function(n){t.close()})}).apply(null,e)}).catch(a.oe)}else(0,s.showMessage)((0,s.translate)("view_influence_diagram_access_denied"),(0,s.translate)("no_permissions"),"error")};__currentSession.modelInfo.uri!=t&&""!=__currentSession.modelInfo.uri?Promise.resolve().then(function(){var n=[a(219)];(function(n){(new n).closeModel(function(){o.removeTask(i),c(t)})}).apply(null,n)}).catch(a.oe):c(t)},openSilentMode:function(n,t,r,o){var i=this;n||(n=this.currentModelUri),o||(this.currentModelUri="_no_model_name_");var s=function(n){i.currentModelUri=n;var o=new e;o.render(),Promise.resolve().then(function(){var e=[a(219)];(function(e){(new e).openModel(n,function(n){o.done(),n&&void 0!=t&&t(n)},r)}).apply(null,e)}).catch(a.oe)};this.currentModelUri!=n&&""!=this.currentModelUri?Promise.resolve().then(function(){var e=[a(219)];(function(e){(new e).closeModel(function(){s(n)})}).apply(null,e)}).catch(a.oe):s(n)},drawToolbar:function(n){var e=new o;return e.setElement(r("#model-summary")),e.render(n),e},showModelSummary:function(){var e=new n,t="report-manager";e.existsTask(t)?e.selectTask(t):(e.addSimpleTask(t,(0,s.translate)("report_manager")),a.e(68).then(function(){var n=[a(874)];(function(n){(new n).render(r("#currentModel").text(),!0)}).apply(null,n)}).catch(a.oe),e.selectTask(t))},clearLastModelOpened:function(){this.currentModelUri="-1"},searchNode:function(n,e){a.e(69).then(function(){var t=[a(794)];(function(a){(new a).render({callback:n,extraClasses:e})}).apply(null,t)}).catch(a.oe)},searchFilteredNodes:function(n){a.e(69).then(function(){var e=[a(794)];(function(e){(new e).render({callback:n,extraClasses:["all","variable","constant"]})}).apply(null,e)}).catch(a.oe)},exportNode:function(n,e){a.e(205).then(function(){var t=[a(948)];(function(a){new a({node:n,nodeQuery:e}).render()}).apply(null,t)}).catch(a.oe)},inputNewModelName:function(){a.e(206).then(function(){var n=[a(949)];(function(n){(new n).render()}).apply(null,n)}).catch(a.oe)},newEmptyModel:function(){a.e(207).then(function(){var n=[a(950)];(function(n){(new n).render()}).apply(null,n)}).catch(a.oe)},showNodeSharer:function(n,e){a.e(208).then(function(){var t=[a(951)];(function(a){(new a).render(n,e)}).apply(null,t)}).catch(a.oe)},showModelInfo:function(){a.e(209).then(function(){var n=[a(952)];(function(n){(new n).render()}).apply(null,n)}).catch(a.oe)},showMsgBox:function(n){var e=n.body;if(e&&3==e.split(",").length){var t=e.split(","),r=t[2],o=t[0];a.e(17).then(function(){var n=[a(685)];(function(n){(new n).show({title:r,text:o,notifyClass:"ademsg"})}).apply(null,n)}).catch(a.oe)}},showProgressBar:function(n){var e=n.body;if(e&&3==e.split(",").length){var t=e.split(","),r=t[0],o=t[1],i=t[2];i*=100,a.e(17).then(function(){var n=[a(685)];(function(n){(new n).show({title:r,text:o,notifyClass:"ademsg",progressBar:i,timeOut:-1,buttons:[{title:(0,s.translate)("cancel"),css:"grey",code:"cancel"}],callback:function(n){"cancel"==n&&Promise.resolve().then(function(){var n=[a(219)];(function(n){(new n).abortProcess()}).apply(null,n)}).catch(a.oe)}})}).apply(null,n)}).catch(a.oe)}},quickEvaluate:function(n){a.e(210).then(function(){var e=[a(953)];(function(e){new e(n).render()}).apply(null,e)}).catch(a.oe)},openDocumentationModal:function(n){a.e(211).then(function(){var e=[a(954)];(function(e){new e(n).render()}).apply(null,e)}).catch(a.oe)}})}.apply(e,o))||(n.exports=i)}).call(this,a(694),a(1))},762:function(n,e,a){"use strict";(function(t,r){var o,i,s=a(18);o=[a(683),a(779)],void 0===(i=function(n,e){return t.View.extend({el:r("#main"),is_done:!1,render:function(a){var t=this,o=e(),i=new n,l=r("#main");void 0!=a&&a.custom_el&&(l=a.custom_el),i.show({title:(0,s.translate)("starting_environment"),html:o,custom_el:l,modalClass:"",backdrop:"static",keyboard:!1,onLoad:function(){r("#main-modal button.close").hide();var n=3,e=0;!function a(){if(0!=r("#main-modal").length)if(t.is_done)t.updateProgressbar(100),r("#main-modal .loading_progress").text("Done!"),setTimeout(function(){r("#main-modal button.close").click()},200);else{(e+=n)>=99&&(e=99),t.updateProgressbar(e);var o="";switch(!0){case e<30:o=(0,s.translate)("creating_environment")+"...";break;case e<60:o=(0,s.translate)("starting_environment")+"...";break;case e<85:o=(0,s.translate)("loading_workspace")+"...",n=1.5;break;case e<96:n=.5,o=(0,s.translate)("starting_pyplan_calc_engine")+"...";break;case e<=100:n=.2,o=(0,s.translate)("opening_model")+"..."}r("#main-modal .loading_progress").text(o),setTimeout(a,500)}}()}})},updateProgressbar:function(n){r("#main-modal .progress-bar").css("width",n+"%")},close:function(){r("#main-modal button.close").click()},done:function(){this.is_done=!0}})}.apply(e,o))||(n.exports=i)}).call(this,a(218),a(1))},763:function(n,e,a){"use strict";(function(t,r){var o,i;o=[a(219),a(780),a(781)],void 0===(i=function(n,e,a){return t.View.extend({el:r("#model-summary"),scrolling:!1,render:function(n){var a=e();this.$el.append(a),r("#swiperchanger button").click(function(){return r("#swiperchanger button").removeClass("active"),r(this).addClass("active"),r(".swiper-container.dashboard-gallery").hide(),r(".swiper-container.dashboard-gallery."+r(this).attr("data-rel")).show(),!1}),void 0!=n&&n()},fillSwipper:function(n){var e=a(n);r(".dashboard-gallery div.swiper-wrapper").html(e)},addItems:function(n){var e=a(n);r(".dashboard-gallery div.swiper-wrapper").append(e),this.refreshDashSwiper()},initDashSwiper:function(){var n=!1;function e(a,t){var o=parseInt(r(a).css("marginLeft").replace("px",""));o>=0&&0==t.indexOf("+")?n=!1:Math.abs(o-.7*r(window).width())>r(".dashboard-gallery .swiper-wrapper").width()&&0==t.indexOf("-")?n=!1:a.animate({marginLeft:t},10,function(){n&&e(a,t)})}r("#right-button-swiper").bind("touchstart mousedown",function(){return n=!0,e(r(".dashboard-gallery .swiper-wrapper"),"-=10px"),!1}),r("#right-button-swiper").bind("touchend mouseup",function(){n=!1}),r("#left-button-swiper").bind("touchstart mousedown",function(){return n=!0,e(r(".dashboard-gallery .swiper-wrapper"),"+=10px"),!1}),r("#left-button-swiper").bind("touchend mouseup",function(){n=!1}),this.refreshDashSwiper()},destroyDashSwiper:function(){r("#right-button-swiper").unbind(),r("#left-button-swiper").unbind()},refreshDashSwiper:function(){var n=30;r(".dashboard-gallery div.swiper-wrapper div.swiper-slide").each(function(){n=n+r(this).width()+10}),r(".dashboard-gallery div.swiper-wrapper").width(n)}})}.apply(e,o))||(n.exports=i)}).call(this,a(218),a(1))},779:function(n,e,a){var t=a(690);n.exports=(t.default||t).template({compiler:[7,">= 4.0.0"],main:function(n,e,a,t,r){return'<div class="row">\n\n  <div class="progress progress-striped active" style="background-color:#f1f1f1; width:80%; margin: 0 auto;">\n    <div class="progress-bar" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="100"\n      style="width: 1%">\n      <span class="sr-only"></span>\n    </div>\n  </div>\n\n</div>\n<div class="row text-center">\n  <h6 class="loading_progress"></h6>\n</div>'},useData:!0})},780:function(n,e,a){var t=a(690);n.exports=(t.default||t).template({compiler:[7,">= 4.0.0"],main:function(n,e,t,r,o){return'    <div class="row-fluid bottom-anchor nodisplay dashboardswiper">\n        <div class="span12">\n            <div class="box">\n        <div class="box-title btn-toolbar">\n\n          <div class="row">\n            <div class="col-sm-5">\n              <div id="swiperchanger" class="btn-group">\n                <button class="btn " data-rel="swiper-dashboard" ><i class="fa fa-bar-chart"></i> '+n.escapeExpression(function(n){return n&&(n.__esModule?n.default:n)}(a(688)).call(null!=e?e:n.nullContext||{},"dashboards",{name:"L",hash:{},data:o}))+'</button>\n              </div>\n\n          </div>\n\n\n        </div>\n\n\n\n        <div class="box-content nopadding swiper-container dashboard-gallery swiper-dashboard">\n          <div  id="left-button-swiper" class="left-button left-button-dashboard">\n            <i class="fa fa-chevron-left"></i>\n          </div>\n          <div class="swiper-wrapper"></div>\n\n          <div  id="right-button-swiper" class="right-button right-button-dashboard">\n            <i class="fa fa-chevron-right"></i>\n          </div>\n        </div>\n\n\n            </div>\n        </div>\n    </div>\n\n\n\n\n\n'},useData:!0})},781:function(n,e,a){var t=a(690);n.exports=(t.default||t).template({1:function(n,e,t,r,o){var i=n.lambda,s=n.escapeExpression;return'<div class="swiper-slide dashboard-slide" data-id="'+s(i(null!=e?e.dashboardId:e,e))+'">\n    \x3c!--img src="'+s(function(n){return n&&(n.__esModule?n.default:n)}(a(718)).call(null!=e?e:n.nullContext||{},{name:"baseURL",hash:{},data:o}))+"thumbs/view.ashx?img=dashboards-common-dash"+s(i(null!=e?e.dashboardId:e,e))+'&w=110&h=53&t=crop" height="53" width="110" alt=""--\x3e\n    <div class="title"><span>'+s(i(null!=e?e.name:e,e))+"</span></div>\n</div>"},compiler:[7,">= 4.0.0"],main:function(n,e,a,t,r){var o;return null!=(o=a.each.call(null!=e?e:n.nullContext||{},null!=e?e.free:e,{name:"each",hash:{},fn:n.program(1,r,0),inverse:n.noop,data:r}))?o:""},useData:!0})}}]);