/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[84],{1645:function(e,n,a){"use strict";(function(t){var o,c;o=[a(664)],void 0===(c=function(e){return t.Controller.extend({name:"dashboardFormatter",getFormatter:function(e,n){var t="";switch(e.substring(0,3)){case"are":t="area/";break;case"col":case"bar":t="columnAndBar/";break;case"lin":t="line/";break;case"tab":t="table/";break;case"pie":t="pie/";break;case"gau":t="gauge/";break;case"wat":t="waterfall/";break;case"sca":t="scatterAndBooble/";break;case"map":t="map/";break;case"ind":t=e.indexOf("indicator")>=0?"indicator/":"index/"}""!=t&&a.e(98).then((function(){var o=[a(2672)("./"+t+e+"Formatter")];(function(e){n(e)}).apply(null,o)})).catch(a.oe)},showConfigCategoriesPopup:function(e){a.e(191).then((function(){var n=[a(2692)];(function(n){(new n).render(e)}).apply(null,n)})).catch(a.oe)},showConditionalFormatPopup:function(e,n){a.e(190).then((function(){var t=[a(2693)];(function(a){(new a).render(e,n)}).apply(null,t)})).catch(a.oe)},showMapEventsPopup:function(e){a.e(189).then((function(){var n=[a(2695)];(function(n){(new n).render(e)}).apply(null,n)})).catch(a.oe)}})}.apply(n,o))||(e.exports=c)}).call(this,a(677))}}]);