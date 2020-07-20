/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{682:function(n,e,t){"use strict";(function(a,o){var r,i,s=t(18);r=[t(664),t(780),t(781)],void 0===(i=function(n,e,r){return a.Controller.extend({name:"modelManager",currentModelUri:"",setCurrentUri:function(n){this.currentModelUri=n},open:function(n,e){e&&(this.currentModelUri="_no_model_name_"),this.openSummary(n)},openSummary:function(a){var r=new n,i="",l=this,c=function(n){if(l.currentModelUri=n,r.existsTask(i))r.selectTask(i);else if((0,s.haveAccess)("view_influence_diagram")){var a=new e;a.render(),Promise.resolve().then((function(){var e=[t(220)];(function(e){(new e).openModel(n,(function(n){if(a.done(),o("#mainLoading").hide(),n)switch(o("#navigation .modelopened").show(),o("#left .navigation .modelopened").show(),n.onOpenModel){case"openDiagram":case"":i="influence_diagram",r.addSimpleTask(i,(0,s.translate)("model")),Promise.all([t.e(12),t.e(17),t.e(21)]).then((function(){var n=[t(698)];(function(n){(new n).showDiagram()}).apply(null,n)})).catch(t.oe),r.selectTask(i);break;case"openReportManager":t.e(52).then((function(){var n=[t(783)];(function(n){(new n).show()}).apply(null,n)})).catch(t.oe);break;case"openDashboard":t.e(32).then((function(){var e=[t(688)];(function(e){(new e).showDashboard(n.onOpenDashId,null,"",!1,!0,null,null)}).apply(null,e)})).catch(t.oe)}}),!1,(function(n){a.close()}))}).apply(null,e)})).catch(t.oe)}else(0,s.showMessage)((0,s.translate)("view_influence_diagram_access_denied"),(0,s.translate)("no_permissions"),"error")};__currentSession.modelInfo.uri!=a&&""!=__currentSession.modelInfo.uri?Promise.resolve().then((function(){var n=[t(220)];(function(n){(new n).closeModel((function(){r.removeTask(i),c(a)}))}).apply(null,n)})).catch(t.oe):c(a)},openSilentMode:function(n,a,o,r){var i=this;n||(n=this.currentModelUri),r||(this.currentModelUri="_no_model_name_");var s=function(n){i.currentModelUri=n;var r=new e;r.render(),Promise.resolve().then((function(){var e=[t(220)];(function(e){(new e).openModel(n,(function(n){r.done(),n&&null!=a&&a(n)}),o)}).apply(null,e)})).catch(t.oe)};this.currentModelUri!=n&&""!=this.currentModelUri?Promise.resolve().then((function(){var e=[t(220)];(function(e){(new e).closeModel((function(){s(n)}))}).apply(null,e)})).catch(t.oe):s(n)},drawToolbar:function(n){var e=new r;return e.setElement(o("#model-summary")),e.render(n),e},showModelSummary:function(){var e=new n,a="report-manager";e.existsTask(a)||(e.addSimpleTask(a,(0,s.translate)("report_manager")),t.e(59).then((function(){var n=[t(887)];(function(n){(new n).render(o("#currentModel").text(),!0)}).apply(null,n)})).catch(t.oe)),e.selectTask(a)},clearLastModelOpened:function(){this.currentModelUri="-1"},searchNode:function(n,e){t.e(79).then((function(){var a=[t(821)];(function(t){(new t).render({callback:n,extraClasses:e})}).apply(null,a)})).catch(t.oe)},searchFilteredNodes:function(n){t.e(79).then((function(){var e=[t(821)];(function(e){(new e).render({callback:n,extraClasses:["all","variable","constant"]})}).apply(null,e)})).catch(t.oe)},exportNode:function(n,e){t.e(181).then((function(){var a=[t(1043)];(function(t){new t({node:n,nodeQuery:e}).render()}).apply(null,a)})).catch(t.oe)},inputNewModelName:function(){t.e(265).then((function(){var n=[t(1044)];(function(n){(new n).render()}).apply(null,n)})).catch(t.oe)},newEmptyModel:function(){t.e(255).then((function(){var n=[t(1045)];(function(n){(new n).render()}).apply(null,n)})).catch(t.oe)},showNodeSharer:function(n,e){t.e(149).then((function(){var a=[t(1046)];(function(t){(new t).render(n,e)}).apply(null,a)})).catch(t.oe)},showModelInfo:function(){t.e(264).then((function(){var n=[t(1047)];(function(n){(new n).render()}).apply(null,n)})).catch(t.oe)},showMsgBox:function(n){var e=n.body;if(e&&3==e.split(",").length){var a=e.split(","),o=a[2],r=a[0];t.e(18).then((function(){var n=[t(665)];(function(n){(new n).show({title:o,text:r,notifyClass:"ademsg"})}).apply(null,n)})).catch(t.oe)}},showProgressBar:function(n){n&&t.e(18).then((function(){var e=[t(665)];(function(e){(new e).show({text:n.message,progressBar:n.progress,notifyClass:"ademsg",timeOut:-1})}).apply(null,e)})).catch(t.oe)},quickEvaluate:function(n){t.e(166).then((function(){var e=[t(1048)];(function(e){new e(n).render()}).apply(null,e)})).catch(t.oe)},debugNode:function(n){t.e(262).then((function(){var e=[t(1049)];(function(e){new e(n).render()}).apply(null,e)})).catch(t.oe)},openDocumentationModal:function(n){t.e(263).then((function(){var e=[t(1050)];(function(e){new e(n).render()}).apply(null,e)})).catch(t.oe)}})}.apply(e,r))||(n.exports=i)}).call(this,t(677),t(1))},780:function(n,e,t){"use strict";(function(a,o){var r,i,s=t(18);r=[t(663),t(798)],void 0===(i=function(n,e){return a.View.extend({el:o("#main"),render:function(t){var a=this,r=e(),i=new n,l=null!=t&&t.custom_el?t.custom_el:o("#main");i.show({title:(0,s.translate)("starting_environment"),html:r,custom_el:l,modalClass:"",backdrop:"static",keyboard:!1,onLoad:function(){var n=o("#main-modal");n.find("button.close").hide(),n.on("progress",(function(e,t){var o=t.title,r=t.message;n.find(".loading_progress").text("".concat((0,s.translate)(o)," ...")),a.updateProgressbar(r)}))}})},updateProgressbar:function(n){var e=this;o("#main-modal .progress-bar").css("width","".concat(n,"%")),100===n&&setTimeout((function(){e.close()}),200)},close:function(){o("body").removeClass("modal-open"),o("#main-modal button.close").click()},done:function(){this.updateProgressbar(100)}})}.apply(e,r))||(n.exports=i)}).call(this,t(219),t(1))},781:function(n,e,t){"use strict";(function(a,o){var r,i;r=[t(220),t(799),t(800)],void 0===(i=function(n,e,t){return a.View.extend({el:o("#model-summary"),scrolling:!1,render:function(n){var t=e();this.$el.append(t),o("#swiperchanger button").click((function(){return o("#swiperchanger button").removeClass("active"),o(this).addClass("active"),o(".swiper-container.dashboard-gallery").hide(),o(".swiper-container.dashboard-gallery."+o(this).attr("data-rel")).show(),!1})),null!=n&&n()},fillSwipper:function(n){var e=t(n);o(".dashboard-gallery div.swiper-wrapper").html(e)},addItems:function(n){var e=t(n);o(".dashboard-gallery div.swiper-wrapper").append(e),this.refreshDashSwiper()},initDashSwiper:function(){var n=!1;function e(t,a){var r=parseInt(o(t).css("marginLeft").replace("px",""));r>=0&&0==a.indexOf("+")||Math.abs(r-.7*o(window).width())>o(".dashboard-gallery .swiper-wrapper").width()&&0==a.indexOf("-")?n=!1:t.animate({marginLeft:a},10,(function(){n&&e(t,a)}))}o("#right-button-swiper").bind("touchstart mousedown",(function(){return n=!0,e(o(".dashboard-gallery .swiper-wrapper"),"-=10px"),!1})),o("#right-button-swiper").bind("touchend mouseup",(function(){n=!1})),o("#left-button-swiper").bind("touchstart mousedown",(function(){return n=!0,e(o(".dashboard-gallery .swiper-wrapper"),"+=10px"),!1})),o("#left-button-swiper").bind("touchend mouseup",(function(){n=!1})),this.refreshDashSwiper()},destroyDashSwiper:function(){o("#right-button-swiper").unbind(),o("#left-button-swiper").unbind()},refreshDashSwiper:function(){var n=30;o(".dashboard-gallery div.swiper-wrapper div.swiper-slide").each((function(){n=n+o(this).width()+10})),o(".dashboard-gallery div.swiper-wrapper").width(n)}})}.apply(e,r))||(n.exports=i)}).call(this,t(219),t(1))},798:function(n,e,t){var a=t(670);n.exports=(a.default||a).template({compiler:[8,">= 4.3.0"],main:function(n,e,t,a,o){return'<div class="row">\n\n  <div class="progress progress-striped active" style="background-color:#f1f1f1; width:80%; margin: 0 auto;">\n    <div class="progress-bar" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="100"\n      style="width: 1%">\n      <span class="sr-only"></span>\n    </div>\n  </div>\n\n</div>\n<div class="row text-center">\n  <h6 class="loading_progress"></h6>\n</div>'},useData:!0})},799:function(n,e,t){var a=t(670);n.exports=(a.default||a).template({compiler:[8,">= 4.3.0"],main:function(n,e,a,o,r){return'    <div class="row-fluid bottom-anchor nodisplay dashboardswiper">\n        <div class="span12">\n            <div class="box">\n        <div class="box-title btn-toolbar">\n\n          <div class="row">\n            <div class="col-sm-5">\n              <div id="swiperchanger" class="btn-group">\n                <button class="btn " data-rel="swiper-dashboard" ><i class="fa fa-bar-chart"></i> '+n.escapeExpression((i=t(668),i&&(i.__esModule?i.default:i)).call(null!=e?e:n.nullContext||{},"dashboards",{name:"L",hash:{},data:r,loc:{start:{line:9,column:98},end:{line:9,column:116}}}))+'</button>\n              </div>\n\n          </div>\n\n\n        </div>\n\n\n\n        <div class="box-content nopadding swiper-container dashboard-gallery swiper-dashboard">\n          <div  id="left-button-swiper" class="left-button left-button-dashboard">\n            <i class="fa fa-chevron-left"></i>\n          </div>\n          <div class="swiper-wrapper"></div>\n\n          <div  id="right-button-swiper" class="right-button right-button-dashboard">\n            <i class="fa fa-chevron-right"></i>\n          </div>\n        </div>\n\n\n            </div>\n        </div>\n    </div>\n\n\n\n\n\n';var i},useData:!0})},800:function(n,e,t){var a=t(670);n.exports=(a.default||a).template({1:function(n,e,a,o,r){var i,s=n.lambda,l=n.escapeExpression,c=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return'<div class="swiper-slide dashboard-slide" data-id="'+l(s(null!=e?c(e,"dashboardId"):e,e))+'">\n    \x3c!--img src="'+l((i=t(712),i&&(i.__esModule?i.default:i)).call(null!=e?e:n.nullContext||{},{name:"baseURL",hash:{},data:r,loc:{start:{line:2,column:17},end:{line:2,column:28}}}))+"thumbs/view.ashx?img=dashboards-common-dash"+l(s(null!=e?c(e,"dashboardId"):e,e))+'&w=110&h=53&t=crop" height="53" width="110" alt=""--\x3e\n    <div class="title"><span>'+l(s(null!=e?c(e,"name"):e,e))+"</span></div>\n</div>"},compiler:[8,">= 4.3.0"],main:function(n,e,t,a,o){var r,i=n.lookupProperty||function(n,e){if(Object.prototype.hasOwnProperty.call(n,e))return n[e]};return null!=(r=i(t,"each").call(null!=e?e:n.nullContext||{},null!=e?i(e,"free"):e,{name:"each",hash:{},fn:n.program(1,o,0),inverse:n.noop,data:o,loc:{start:{line:1,column:0},end:{line:4,column:15}}}))?r:""},useData:!0})}}]);