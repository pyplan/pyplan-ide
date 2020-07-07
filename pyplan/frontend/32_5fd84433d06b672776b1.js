/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[32],{687:function(e,a,n){"use strict";(function(t,c){var o,r;o=[n(664)],void 0===(r=function(e){var a=this;return t.Controller.extend({name:"dashboardManager",showDashboard:function(a,t,o,r,l,i,u){var s="dashboard-".concat(a),h="dashboard-".concat(t),p=new e;p.existsTask(h)&&(s=h),p.existsTask(s)?(p.selectTask(s),r&&c(".mainTask[data-rel='".concat(s,"']")).length>0&&c(".mainTask[data-rel='".concat(s,"']")).trigger("refreshView")):(p.addSimpleTask(s,o),n.e(41).then((function(){var e=[n(869)];(function(e){(new e).render(a,t,l,i,u),p.selectTask(s)}).apply(null,e)})).catch(n.oe))},showEmbeddableDashboard:function(a,t,o,r,l,i){var u="dashboard-".concat(a),s=new e;__currentSession.fromEmbedded,s.existsTask(u)?(s.selectTask(u),r&&c(".mainTask[data-rel='".concat(u,"']")).length>0&&c(".mainTask[data-rel='".concat(u,"']")).trigger("refreshView")):(s.addSimpleTask(u,o),Promise.all([n.e(41),n.e(239)]).then((function(){var e=[n(980)];(function(e){(new e).render(a,t,o,l,i),s.selectTask(u)}).apply(null,e)})).catch(n.oe))},removeDashboardTaskFromHome:function(a){var n="dashboard-".concat(a),t=new e;t.existsTask(n)&&t.removeTask(n)},drawDashboardBars:function(e,n){a.drawToolbar(e,(function(){n()}))},drawBottombar:function(e,a){n.e(206).then((function(){var t=[n(981)];(function(n){var t=new n;t.setElement(e),t.render(),null!=a&&a()}).apply(null,t)})).catch(n.oe)},showNodeInfo:function(e){Promise.all([n.e(12),n.e(17),n.e(78)]).then((function(){var a=[n(812)];(function(a){new a(e).render()}).apply(null,a)})).catch(n.oe)},removeNodeInfo:function(e){Promise.all([n.e(12),n.e(17),n.e(78)]).then((function(){var a=[n(812)];(function(a){(new a).remove(e)}).apply(null,a)})).catch(n.oe)},drawToolbar:function(e,a){n.e(50).then((function(){var t=[n(871)];(function(n){(new n).show({el:e,positions:["left","right"],onLoad:a,className:"dockDashboardProperty"})}).apply(null,t)})).catch(n.oe)},drawMoreDashboard:function(e,a){n.e(238).then((function(){var e=[n(982)];(function(e){var n=new e;n.setElement("body"),n.render(a)}).apply(null,e)})).catch(n.oe)},getDefaultContent:function(e,a){Promise.all([n.e(0),n.e(9),n.e(88)]).then((function(){var t=[n(756)];(function(n){var t=new n({model:e});a(t)}).apply(null,t)})).catch(n.oe)},getEmptyContent:function(e,a){Promise.all([n.e(0),n.e(89)]).then((function(){var t=[n(813)];(function(n){var t=new n({model:e});a(t)}).apply(null,t)})).catch(n.oe)},getChartToolbar:function(e,a,t,c){var o;switch(e){case"linechart":o="line/lineToolbar";break;case"columnchart":case"columnchartstacked":case"columnchartpercent":case"barchart":case"barchartstacked":case"barchartpercent":o="columnAndBar/columnAndBarToolbar";break;case"areachart":case"areachartstacked":case"areachartpercent":o="area/areaToolbar";break;case"piechart":o="pie/pieToolbar";break;case"funnelchart":o="funnelToolbar/funnelToolbar";break;case"pyramidchart":o="pyramidToolbar/pyramidToolbar";break;case"gaugechart":o="gauge/gaugeToolbar";break;case"waterfallchart":o="waterfall/waterfallToolbar";break;case"scatterchart":o="scatter/scatterToolbar";break;case"table":o="table/tableToolbar";break;case"indexlist":o="index/indexToolbar";break;case"map":o="map/mapToolbar";break;case"indicator":o="indicator/indicatorToolbar";break;case"selector":o="selector/selectorToolbar";break;case"formnode":o="formnode/formnodeToolbar";break;case"nodetable":o="nodeTable/nodetableToolbar";break;case"button":o="button/buttonToolbar";break;case"analyticachart":o="analyticaChart/analyticaChartToolbar";break;case"objectItem":switch(a){case"texteditor":o="texteditor/texteditorToolbar";break;case"cubeviewer":o="cubeviewer/cubeviewerToolbar";break;case"diagramviewer":o="diagramViewer/diagramViewerToolbar";break;case"mapviewer":o="mapViewer/mapViewerToolbar";break;case"inputform":o="inputForm/inputFormToolbar";break;case"menuwidget":o="menuWidget/menuWidgetToolbar";break;case"dashboardcontainer_QUITAR_ESTO_PARA_MOSTRAR":o="dashboardContainer/dashboardContainerToolbar"}break;case"complexchart":o="complexchart/complexChartToolbar";break;default:o=!1}o?Promise.all([n.e(25),n.e(95)]).then((function(){var e=[n(983)("./".concat(o))];(function(e){var a=new e({model:t});c(a)}).apply(null,e)})).catch(n.oe):Promise.all([n.e(25),n.e(44),n.e(303)]).then((function(){var e=[n(984)];(function(e){var a=new e({model:t});c(a)}).apply(null,e)})).catch(n.oe)},getChartItemViewFromType:function(e,a){switch(e){case"empty":Promise.all([n.e(0),n.e(89)]).then((function(){var e=[n(813)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"linechart":Promise.all([n.e(0),n.e(9),n.e(294)]).then((function(){var e=[n(985)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"columnchart":Promise.all([n.e(0),n.e(9),n.e(88)]).then((function(){var e=[n(756)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"columnchartstacked":Promise.all([n.e(0),n.e(9),n.e(236)]).then((function(){var e=[n(986)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"columnchartpercent":Promise.all([n.e(0),n.e(9),n.e(235)]).then((function(){var e=[n(987)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"barchart":Promise.all([n.e(0),n.e(9),n.e(290)]).then((function(){var e=[n(815)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"barchartstacked":Promise.all([n.e(0),n.e(9),n.e(234)]).then((function(){var e=[n(988)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"barchartpercent":Promise.all([n.e(0),n.e(9),n.e(233)]).then((function(){var e=[n(989)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"areachart":Promise.all([n.e(0),n.e(9),n.e(289)]).then((function(){var e=[n(816)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"areachartstacked":Promise.all([n.e(0),n.e(9),n.e(232)]).then((function(){var e=[n(990)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"areachartpercent":Promise.all([n.e(0),n.e(9),n.e(231)]).then((function(){var e=[n(991)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"piechart":Promise.all([n.e(0),n.e(9),n.e(295)]).then((function(){var e=[n(992)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"gaugechart":Promise.all([n.e(0),n.e(9),n.e(293)]).then((function(){var e=[n(993)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"waterfallchart":Promise.all([n.e(0),n.e(9),n.e(298)]).then((function(){var e=[n(994)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"scatterchart":Promise.all([n.e(0),n.e(9),n.e(297)]).then((function(){var e=[n(995)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"complexchart":Promise.all([n.e(0),n.e(9),n.e(291)]).then((function(){var e=[n(996)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"table":Promise.all([n.e(0),n.e(12),n.e(120)]).then((function(){var e=[n(997)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"indexlist":Promise.all([n.e(0),n.e(147)]).then((function(){var e=[n(998)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"map":Promise.all([n.e(37),n.e(0),n.e(12),n.e(57),n.e(205)]).then((function(){var e=[n(999)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"indicator":Promise.all([n.e(80),n.e(93),n.e(0),n.e(110)]).then((function(){var e=[n(1e3)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"selector":Promise.all([n.e(0),n.e(119)]).then((function(){var e=[n(1023)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"formnode":Promise.all([n.e(0),n.e(204)]).then((function(){var e=[n(1024)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"nodetable":Promise.all([n.e(0),n.e(15),n.e(28),n.e(237)]).then((function(){var e=[n(1025)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"button":Promise.all([n.e(0),n.e(203)]).then((function(){var e=[n(1026)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"funnelchart":Promise.all([n.e(0),n.e(9),n.e(292)]).then((function(){var e=[n(1027)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"pyramidchart":Promise.all([n.e(0),n.e(9),n.e(296)]).then((function(){var e=[n(1028)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"analyticachart":Promise.all([n.e(0),n.e(230)]).then((function(){var e=[n(1029)];(function(e){a(e)}).apply(null,e)})).catch(n.oe)}},getObjectItemViewFromType:function(e,a){switch(e){case"texteditor":Promise.all([n.e(0),n.e(61),n.e(302)]).then((function(){var e=[n(1030)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"cubeviewer":Promise.all([n.e(0),n.e(15),n.e(28),n.e(299)]).then((function(){var e=[n(1031)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"diagramviewer":Promise.all([n.e(0),n.e(12),n.e(17),n.e(300)]).then((function(){var e=[n(1032)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"mapviewer":Promise.all([n.e(37),n.e(0),n.e(12),n.e(58),n.e(301)]).then((function(){var e=[n(1033)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"inputform":Promise.all([n.e(0),n.e(15),n.e(29),n.e(225)]).then((function(){var e=[n(1034)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);break;case"dashboardcontainer":Promise.all([n.e(0),n.e(240)]).then((function(){var e=[n(1035)];(function(e){a(e)}).apply(null,e)})).catch(n.oe);case"menuwidget":Promise.all([n.e(0),n.e(25),n.e(174)]).then((function(){var e=[n(1036)];(function(e){a(e)}).apply(null,e)})).catch(n.oe)}},getFilterView:function(e){n.e(129).then((function(){var a=[n(1037)];(function(a){e(a)}).apply(null,a)})).catch(n.oe)},showCopyDashboard:function(e,a,t){n.e(187).then((function(){var c=[n(1038)];(function(n){(new n).render(e,a,t)}).apply(null,c)})).catch(n.oe)},showDashboardComments:function(e){n.e(135).then((function(){var a=[n(1039)];(function(a){var n=new a;n.setElement(e.parent),n.render(e)}).apply(null,a)})).catch(n.oe)},refreshAllOpenDashboards:function(){c(".mainTask.dashboardTask .btnRefresh").trigger("click")},showTimeFrameSetting:function(e){n.e(194).then((function(){var a=[n(1040)];(function(a){var n=new a(e);n.setElement(e.el),n.render()}).apply(null,a)})).catch(n.oe)},updatePrintReportProgress:function(e){n.e(46).then((function(){var a=[n(757)];(function(a){new a(e).updatePrintReportProgress()}).apply(null,a)})).catch(n.oe)},updatePrintReportMessage:function(e){n.e(46).then((function(){var a=[n(757)];(function(a){new a(e).updatePrintReportMessage()}).apply(null,a)})).catch(n.oe)},updatePrintReportComplete:function(e){n.e(46).then((function(){var a=[n(757)];(function(a){new a(e).updatePrintReportComplete()}).apply(null,a)})).catch(n.oe)},loginInToMyPyplanModal:function(e){n.e(241).then((function(){var a=[n(1041)];(function(a){(new a).render(e)}).apply(null,a)})).catch(n.oe)},publishToMyPyplanModal:function(e){n.e(198).then((function(){var a=[n(1042)];(function(a){(new a).render(e)}).apply(null,a)})).catch(n.oe)}})}.apply(a,o))||(e.exports=r)}).call(this,n(677),n(1))}}]);