/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[251],{1777:function(e,n,a){"use strict";(function(t){var o,i,r=a(18);o=[a(868),a(691),a(726),a(1778)],void 0===(i=function(e,n,a,o){return e.extend({render:function(e,i,d,s){this.currentDashboardId=e,this.keyView="div.mainTask[data-rel='dashboard-"+e+"']";var l={id:e,extraOptions:s,notDesktop:!1};this.dashboardModel=new a({dashboardViewList:[],nodeOwner:"",extraOptions:s}),this.dashboardController=new n,s&&s.external&&(this.fromExternal=!0);var c=o(l);t('div[data-rel="embeddable"]').append(c),this.getParent().find(".dashboard-area"),this.reloadDashboard(e,d);var u=this;(0,r.registerResizeEvents)("dashboardViewResize",(function(){u.updateSizes()})),this.getParent().on("removeView",(function(){u.onRemoveView()})),this.getParent().on("beforeRemoveView",(function(e,n){u.onBeforeRemoveView(e,n)})),this.getParent().on("refreshView",(function(){u.getParent().find("div.toolbar button.btnRefresh").trigger("click")})),this.getParent().on("changeNumberFormat",(function(e,n){u&&u.dashboardModel&&u.dashboardModel.applyNumberFormat(n)})),this.getParent().on("reevaluateNodesNeeded",(function(e,n){u&&u.dashboardModel&&u.dashboardModel.reevaluateNodesNeededInThisDashboard(n)})),this.getParent().on("selectView",(function(){u.updateSizes()})),this.getParent().on("updateScaleFactor",(function(){var e=u.getParent().find(".main-pane .pane-container").first();u._navigateInPane(e,{})})),this.addHandlers(),this.addGenericHandlers()},refreshDashboardName:function(e){if(e){e.dashboardId;var n=e.name;this.dashboardName=n,t(".dashboard-title li span").text(n)}}})}.apply(n,o))||(e.exports=i)}).call(this,a(1))},1778:function(e,n,a){var t=a(670);e.exports=(t.default||t).template({1:function(e,n,a,t,o){return" from-external "},compiler:[8,">= 4.3.0"],main:function(e,n,a,t,o){var i,r,d=null!=n?n:e.nullContext||{},s=e.hooks.helperMissing,l=e.escapeExpression,c=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'<div class="container-fluid mainTask full-horizontal dashboardTask tab-pane hideClose nodisplay '+(null!=(i=c(a,"if").call(d,null!=(i=null!=n?c(n,"extraOptions"):n)?c(i,"external"):i,{name:"if",hash:{},fn:e.program(1,o,0),inverse:e.noop,data:o,loc:{start:{line:1,column:96},end:{line:1,column:147}}}))?i:"")+'"\n  data-rel="dashboard-'+l("function"==typeof(r=null!=(r=c(a,"id")||(null!=n?c(n,"id"):n))?r:s)?r.call(d,{name:"id",hash:{},data:o,loc:{start:{line:2,column:22},end:{line:2,column:28}}}):r)+'" id="dashboard-'+l("function"==typeof(r=null!=(r=c(a,"id")||(null!=n?c(n,"id"):n))?r:s)?r.call(d,{name:"id",hash:{},data:o,loc:{start:{line:2,column:44},end:{line:2,column:50}}}):r)+'" data-type="tab-content">\n\n  <div class="row-fluid dashboard-area">\n    <div class="main-pane">\n\n    </div>\n\n    <div class="main-fullscreen">\n      <div class="item-toolbar-view">\n        <button class="btn btn-small" data-rel="close-screen">\n          <i class="fa fa-arrows-alt"></i>\n        </button>\n      </div>\n    </div>\n  </div>\n</div>\n'},useData:!0})}}]);