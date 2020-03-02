/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[88,286],{701:function(e,a,n){"use strict";(function(t,r){var c,o;c=[n(684),n(703)],void 0===(o=function(e,a){return t.Controller.extend({name:"dashboardManager",showDashboard:function(a,t,c,o,l,i){var u="dashboard-"+a,s=new e;s.existsTask(u)?(s.selectTask(u),o&&r(".mainTask[data-rel='"+u+"']").length>0&&r(".mainTask[data-rel='"+u+"']").trigger("refreshView")):(s.addSimpleTask(u,c),n.e(20).then(function(){var e=[n(752)];(function(e){(new e).render(a,t,l,i),s.selectTask(u)}).apply(null,e)}).catch(n.oe))},showEmbeddableDashboard:function(a,t,c,o,l,i){var u="dashboard-"+a,s=new e;__currentSession.fromEmbedded&&s.removeAllTask(),s.existsTask(u)?(s.selectTask(u),o&&r(".mainTask[data-rel='"+u+"']").length>0&&r(".mainTask[data-rel='"+u+"']").trigger("refreshView")):(s.addSimpleTask(u,c),Promise.all([n.e(20),n.e(124)]).then(function(){var e=[n(808)];(function(e){(new e).render(a,t,l,i),s.selectTask(u)}).apply(null,e)}).catch(n.oe))},removeDashboardTaskFromHome:function(a){var n="dashboard-"+a,t=new e;t.existsTask(n)&&t.removeTask(n)},drawDashboardBars:function(e,a){this.drawToolbar(e,function(){a()})},drawBottombar:function(e,a){n.e(125).then(function(){var t=[n(809)];(function(n){var t=new n;t.setElement(e),t.render(),void 0!=a&&a()}).apply(null,t)}).catch(n.oe)},drawToolbar:function(e,a){n.e(42).then(function(){var t=[n(748)];(function(n){(new n).show({el:e,positions:["left","right"],onLoad:a,className:"dockDashboardProperty"})}).apply(null,t)}).catch(n.oe)},drawMoreDashboard:function(e,a){n.e(126).then(function(){var e=[n(810)];(function(e){var n=new e;n.setElement("body"),n.render(a)}).apply(null,e)}).catch(n.oe)},getDefaultContent:function(e,a){Promise.all([n.e(1),n.e(8),n.e(62)]).then(function(){var t=[n(727)];(function(n){var t=new n({model:e});a(t)}).apply(null,t)}).catch(n.oe)},getEmptyContent:function(e,a){Promise.all([n.e(1),n.e(63)]).then(function(){var t=[n(741)];(function(n){var t=new n({model:e});a(t)}).apply(null,t)}).catch(n.oe)},getChartToolbar:function(e,a,t,r){var c;switch(e){case"linechart":c="line/lineToolbar";break;case"columnchart":case"columnchartstacked":case"columnchartpercent":case"barchart":case"barchartstacked":case"barchartpercent":c="columnAndBar/columnAndBarToolbar";break;case"areachart":case"areachartstacked":case"areachartpercent":c="area/areaToolbar";break;case"piechart":c="pie/pieToolbar";break;case"funnelchart":c="funnelToolbar/funnelToolbar";break;case"pyramidchart":c="pyramidToolbar/pyramidToolbar";break;case"gaugechart":c="gauge/gaugeToolbar";break;case"waterfallchart":c="waterfall/waterfallToolbar";break;case"scatterchart":c="scatter/scatterToolbar";break;case"table":c="table/tableToolbar";break;case"indexlist":c="index/indexToolbar";break;case"map":c="map/mapToolbar";break;case"indicator":c="indicator/indicatorToolbar";break;case"selector":c="selector/selectorToolbar";break;case"formnode":c="formnode/formnodeToolbar";break;case"nodetable":c="nodeTable/nodetableToolbar";break;case"button":c="button/buttonToolbar";break;case"analyticachart":c="analyticaChart/analyticaChartToolbar";break;case"objectItem":switch(a){case"texteditor":c="texteditor/texteditorToolbar";break;case"cubeviewer":c="cubeviewer/cubeviewerToolbar";break;case"diagramviewer":c="diagramViewer/diagramViewerToolbar";break;case"mapviewer":c="mapViewer/mapViewerToolbar";break;case"menuwidget":c="menuWidget/menuWidgetToolbar";break;case"dashboardcontainer_QUITAR_ESTO_PARA_MOSTRAR":c="dashboardContainer/dashboardContainerToolbar"}break;case"complexchart":c="complexchart/complexChartToolbar";break;default:c=!1}c?Promise.all([n.e(24),n.e(55),n.e(127)]).then(function(){var e=[n(811)("./"+c)];(function(e){var a=new e({model:t});r(a)}).apply(null,e)}).catch(n.oe):Promise.all([n.e(24),n.e(55),n.e(128)]).then(function(){var e=[n(812)];(function(e){var a=new e({model:t});r(a)}).apply(null,e)}).catch(n.oe)},getChartItemViewFromType:function(e,a){switch(e){case"empty":Promise.all([n.e(1),n.e(63)]).then(function(){var e=[n(741)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"linechart":Promise.all([n.e(1),n.e(8),n.e(129)]).then(function(){var e=[n(813)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"columnchart":Promise.all([n.e(1),n.e(8),n.e(62)]).then(function(){var e=[n(727)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"columnchartstacked":Promise.all([n.e(1),n.e(8),n.e(130)]).then(function(){var e=[n(814)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"columnchartpercent":Promise.all([n.e(1),n.e(8),n.e(131)]).then(function(){var e=[n(815)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"barchart":Promise.all([n.e(1),n.e(8),n.e(132)]).then(function(){var e=[n(759)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"barchartstacked":Promise.all([n.e(1),n.e(8),n.e(133)]).then(function(){var e=[n(816)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"barchartpercent":Promise.all([n.e(1),n.e(8),n.e(134)]).then(function(){var e=[n(817)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"areachart":Promise.all([n.e(1),n.e(8),n.e(135)]).then(function(){var e=[n(760)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"areachartstacked":Promise.all([n.e(1),n.e(8),n.e(136)]).then(function(){var e=[n(818)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"areachartpercent":Promise.all([n.e(1),n.e(8),n.e(137)]).then(function(){var e=[n(819)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"piechart":Promise.all([n.e(1),n.e(8),n.e(138)]).then(function(){var e=[n(820)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"gaugechart":Promise.all([n.e(1),n.e(8),n.e(139)]).then(function(){var e=[n(821)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"waterfallchart":Promise.all([n.e(1),n.e(8),n.e(140)]).then(function(){var e=[n(822)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"scatterchart":Promise.all([n.e(1),n.e(8),n.e(141)]).then(function(){var e=[n(823)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"complexchart":Promise.all([n.e(1),n.e(8),n.e(142)]).then(function(){var e=[n(824)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"table":Promise.all([n.e(1),n.e(11),n.e(143)]).then(function(){var e=[n(825)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"indexlist":Promise.all([n.e(1),n.e(144)]).then(function(){var e=[n(826)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"map":Promise.all([n.e(33),n.e(1),n.e(11),n.e(93),n.e(145)]).then(function(){var e=[n(827)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"indicator":Promise.all([n.e(91),n.e(1),n.e(146)]).then(function(){var e=[n(828)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"selector":Promise.all([n.e(1),n.e(147)]).then(function(){var e=[n(829)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"formnode":Promise.all([n.e(1),n.e(148)]).then(function(){var e=[n(830)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"nodetable":Promise.all([n.e(1),n.e(15),n.e(34),n.e(149)]).then(function(){var e=[n(831)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"button":Promise.all([n.e(1),n.e(150)]).then(function(){var e=[n(832)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"funnelchart":Promise.all([n.e(1),n.e(8),n.e(151)]).then(function(){var e=[n(833)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"pyramidchart":Promise.all([n.e(1),n.e(8),n.e(152)]).then(function(){var e=[n(834)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"analyticachart":Promise.all([n.e(1),n.e(153)]).then(function(){var e=[n(835)];(function(e){a(e)}).apply(null,e)}).catch(n.oe)}},getObjectItemViewFromType:function(e,a){switch(e){case"texteditor":Promise.all([n.e(1),n.e(92),n.e(154)]).then(function(){var e=[n(836)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"cubeviewer":Promise.all([n.e(1),n.e(15),n.e(34),n.e(155)]).then(function(){var e=[n(837)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"diagramviewer":Promise.all([n.e(1),n.e(11),n.e(16),n.e(156)]).then(function(){var e=[n(838)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"mapviewer":Promise.all([n.e(33),n.e(1),n.e(11),n.e(94),n.e(157)]).then(function(){var e=[n(839)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"inputform":Promise.all([n.e(1),n.e(15),n.e(35),n.e(158)]).then(function(){var e=[n(840)];(function(e){a(e)}).apply(null,e)}).catch(n.oe);break;case"dashboardcontainer":Promise.all([n.e(1),n.e(159)]).then(function(){var e=[n(841)];(function(e){a(e)}).apply(null,e)}).catch(n.oe)}},getFilterView:function(e){n.e(160).then(function(){var a=[n(842)];(function(a){e(a)}).apply(null,a)}).catch(n.oe)},showCopyDashboard:function(e,a,t){n.e(161).then(function(){var r=[n(843)];(function(n){(new n).render(e,a,t)}).apply(null,r)}).catch(n.oe)},showDashboardComments:function(e){n.e(162).then(function(){var a=[n(844)];(function(a){var n=new a;n.setElement(e.parent),n.render(e)}).apply(null,a)}).catch(n.oe)},refreshAllOpenDashboards:function(){r(".mainTask.dashboardTask .btnRefresh").trigger("click")},showTimeFrameSetting:function(e){n.e(163).then(function(){var a=[n(845)];(function(a){var n=new a(e);n.setElement(e.el),n.render()}).apply(null,a)}).catch(n.oe)},updatePrintReportProgress:function(e){n.e(43).then(function(){var a=[n(720)];(function(a){new a(e).updatePrintReportProgress()}).apply(null,a)}).catch(n.oe)},updatePrintReportMessage:function(e){n.e(43).then(function(){var a=[n(720)];(function(a){new a(e).updatePrintReportMessage()}).apply(null,a)}).catch(n.oe)},updatePrintReportComplete:function(e){n.e(43).then(function(){var a=[n(720)];(function(a){new a(e).updatePrintReportComplete()}).apply(null,a)}).catch(n.oe)}})}.apply(a,c))||(e.exports=o)}).call(this,n(694),n(1))}}]);