/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[157],{839:function(t,e,i){"use strict";(function(s){var r,n;i(886),L.Icon.Default.imagePath="leaflet",r=[i(731),i(1187),i(1188)],void 0===(n=function(t,e,i){return t.extend({el:s("#n_o_n_e"),mapView:void 0,rememberRefresh:!1,render:function(t){this.baseRender(t),this.drawItem()},editModeChanged:function(){this.editMode?this.rememberRefresh=!0:(this.rememberRefresh&&this.refreshItemDash(),this.rememberRefresh=!1)},refreshItemDash:function(){this.fullRefresh()},getNodesOfView:function(){if(this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.mapOptions&&this.currentResult.itemProperties.mapOptions.layers&&this.currentResult.itemProperties.mapOptions.layers.length>0){for(var t=[],e=this.currentResult.itemProperties.mapOptions.layers,i=0;i<e.length;i++)e[i].options&&e[i].options.node&&t.push(e[i].options.node);return e=null,t}},needRefresh:function(t){if(this.currentResult&&this.currentResult.itemProperties&&this.currentResult.itemProperties.mapOptions&&this.currentResult.itemProperties.mapOptions.layers&&this.currentResult.itemProperties.mapOptions.layers.length>0){for(var e=this.currentResult.itemProperties.mapOptions.layers,i=0;i<t.length;i++)for(var s=0;s<e.length;s++)if(e[s].options&&e[s].options.node&&t[i].toLowerCase()==e[s].options.node.toLowerCase())return!0;e=null}return!1},baseUpdateSize:function(){s(this.tagId).find(".item-area").height(s(this.tagId).parent().height()),s(this.tagId).find(".item-area").css("top","0px")},drawItem:function(){s(this.tagId).find(".item-area").addClass("extrafullSize"),s(this.tagId).find(".item-title").remove(),this.setDefaultOptions();var t=this.currentResult.itemProperties.mapOptions;t&&(t.startBaseMap=0);var r=this.tagId.substr(1)+"_map",n=i({mapElementId:r});s(this.tagId).find(".item-area").html(n),this.updateSize(),this.mapView=new e(t),this.mapView.setElement("#"+r),this.mapView.setDashboardMoldel(this.model),this.mapView.render(),this.addHandlers(),this.isReady=!0},fullRefresh:function(){if(this.mapView){this.setDefaultOptions();var t=this.currentResult.itemProperties.mapOptions;t.initLat&&t.initLng&&(t.startBaseMap=0,t.center={lat:t.initLat,lng:t.initLng},t.autCenter=t.autCenter,this.mapView.setOptions(t)),t&&t.layers&&t.layers&&(t.startBaseMap=0,this.mapView.setOptions(t),this.mapView.drawLayers())}},onRemoveItemView:function(){this.mapView&&(this.mapView.destroy(),this.mapView=null)},updateValues:function(t){},_evaluateNode:function(t,e,i,s,r){},updateSize:function(){s(this.tagId).find(".item-area").height(s(this.tagId).parent().height()-7),this.mapView&&this.mapView.onResize()},setDefaultOptions:function(){this.currentResult||(this.currentResult={}),this.currentResult.itemProperties||(this.currentResult.itemProperties={}),this.currentResult.itemProperties.mapOptions||(this.currentResult.itemProperties.mapOptions={maxZoom:17,initZoom:10,initLat:"auto",initLng:"auto",showControlLayer:!0,startBaseMap:0,autCenter:!0},this.currentResult.itemProperties.mapOptions.autCenter||(this.currentResult.itemProperties.mapOptions.autCenter=!0))},addHandlers:function(){var t=this;s(this.tagId).find(".btn-maximize-map").on("click",function(){s(this).closest("div.main-fullscreen").length>0?s(this).closest("div.main-fullscreen").find("button[data-rel='close-screen']").click():t.fullScreen()})}})}.apply(e,r))||(t.exports=n)}).call(this,i(1))}}]);