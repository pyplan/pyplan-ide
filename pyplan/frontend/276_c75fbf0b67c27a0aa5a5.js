/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[276],{2076:function(e,i,t){"use strict";(function(o,d){var a,n;a=[t(2077)],void 0===(n=function(e){return o.View.extend({el:d("#main"),defaults:{positions:["left","right","top","bottom"]},initialize:function(){this.options=d.extend({},this.defaults,this.options)},render:function(){var i=this,t=this.options;t||(t={}),t.hasOwnProperty("id")||(t.id=d.uuid());var o="#"+t.id,a=e(t);this.$el.append(a),this.setDockPosition(o),t.hasOwnProperty("html")&&d(o).find(".dock-container").html(t.html),t.hasOwnProperty("onLoad")&&t.onLoad(d(o)),this.addDraggable(d(o)),this.addResizable(d(o)),d(o).on("updateTitle",function(e,i){d(this).find(".header h3").text(i)}),d(".dockInfluenceDiagramProperty").on("updateWidth",function(e){i.dockedWindowWidth=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width();i.maxCodeWidth=70*i.dockedWindowWidth/100,d(".codeArea").resizable("option","maxWidth",i.maxCodeWidth),d("#nodeWizardEval").width(i.dockedWindowWidth-i.$el.find(".codeArea").width()-12),i.$el.find(".resultArea").width(i.dockedWindowWidth-i.$el.find(".codeArea").width()-12)}),d(".dockCommandBtns i").on("click",function(e){switch(e.currentTarget.getAttribute("data-action")){case"minimize":d(".dock.dockItem").addClass("bottom").addClass("docked"),d(".dock.dockItem").css({left:"",top:"",height:"",width:""}),d(".dockInfluenceDiagramProperty").trigger("updateSizesOnDock"),d(".nodeDocumentationTab").trigger("updateSizes"),d(".nodeInputOutputTab").trigger("updateSizes"),d(".nodePropertiesTab").trigger("updateSizes"),d(".nodeWizardTab").trigger("updateSizes");break;case"maximize":var i=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").parent().width()-100,t=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").parent().height();d(".dock.dockItem").addClass("top").removeClass("docked"),d(".dock.dockItem").css({left:"",top:"",height:"".concat(t,"px"),width:"".concat(i,"px")}),d(".dockInfluenceDiagramProperty").trigger("updateSizesOnDock"),d(".nodeDocumentationTab").trigger("updateSizes"),d(".nodeInputOutputTab").trigger("updateSizes"),d(".nodePropertiesTab").trigger("updateSizes"),d(".nodeWizardTab").trigger("updateSizes")}})},addDraggable:function(e){var i=this,t=!1;e.on("mousemove",".dragger",function(e){t&&d(this).closest(".dock").hasClass("docked")&&(d.inArray("top",i.options.positions)>0||d.inArray("bottom",i.options.positions)>0?d(this).closest(".dock").height(255).width(.7*i.$el.width()):d(this).closest(".dock").height(.7*i.$el.height()).width(300),d(".nodePropertiesTab").trigger("updateSizes")),t=!1}).on("mousedown",".dragger",function(e){d(e.target).hasClass("dockMaximize")||d(e.target).hasClass("dockMinimize")||(t=!0)}).on("mouseup",".dragger",function(e){d(e.target).hasClass("dockMaximize")||d(e.target).hasClass("dockMinimize")||(t=!1)}),e.draggable({handle:".dragger",scroll:!1,containment:"parent",opacity:.35,refreshPositions:!0,start:function(e,t){var o=t.helper;o.hasClass("docked")&&(d.inArray("top",i.options.positions)>0||d.inArray("bottom",i.options.positions)>0?o.height(255).width(.7*i.$el.width()):o.height(.7*i.$el.height()).width(300)),o.removeClass("docked").removeClass("left").removeClass("right").removeClass("top").removeClass("bottom")},drag:function(e,t){var o=i.getDockZone(t);if(""==o)i.$el.find(".dockPosition").remove();else{0==i.$el.find(".dockPosition").length?i.$el.append("<div class='dockPosition dockItem "+o+"'></div>"):(i.$el.find(".dockPosition").removeClass("left").removeClass("right").removeClass("top").removeClass("bottom"),i.$el.find(".dockPosition").addClass(o));var a=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").parent().width();i.$el.find(".dockPosition").width(a-100)}},stop:function(t,o){i.$el.find(".dockPosition").remove();var a=i.getDockZone(o);""!=a?(o.helper.css({left:"",top:"",height:"",width:""}),o.helper.addClass(a).addClass("docked"),d(".dockInfluenceDiagramProperty").trigger("updateSizesOnDock")):(t.clientY<0?o.helper.css("top",0):t.clientY+25>d(window).height()&&o.helper.css("top",d(window).height()-50),d(".nodeDocumentationTab").trigger("updateSizes")),d(".nodeWizardTab").trigger("updateSizes"),i.addResizable(e),i.saveDockPosition(e,a)}})},getDockZone:function(e){var i=0;e.helper.parent().position().left&&(i=e.helper.parent().position().left);var t="";return this.options.positions.indexOf("left")>=0&&e.offset.left<80+i?t="left":this.options.positions.indexOf("right")>=0&&e.offset.left+e.helper.width()>this.$el.width()-80+i?t="right":this.options.positions.indexOf("top")>=0&&e.offset.top<60?t="top":this.options.positions.indexOf("bottom")>=0&&e.offset.top+e.helper.height()>this.$el.height()-60&&(t="bottom"),t},addResizable:function(e){var i=this;e.hasClass("ui-resizable")&&e.resizable("destroy"),d(".codeArea").resizable("destroy"),i.dockedWindowWidth=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width();d(".resultPreview").width(),d(".leftCol").width();var t=0;if(d("#nodeWizardDef").length>0){i.dockedWindowWidth=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width();i.maxCodeWidth=70*i.dockedWindowWidth/100,t=i.maxCodeWidth;var o=d.cookie("resultAreaWidth")?i.dockedWindowWidth-parseInt(d.cookie("resultAreaWidth")):t;d.cookie("resultAreaWidth")&&parseInt(d.cookie("resultAreaWidth"))<=i.maxCodeWidth&&(t=o),i.$el.find(".codeArea").width(t),i.dockedWindowWidth=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width(),i.maxCodeWidth=70*i.dockedWindowWidth/100,d("#nodeWizardEval").width(i.dockedWindowWidth-t-12),i.$el.find(".resultArea").width(i.dockedWindowWidth-t-12),d(".codeArea").resizable({minWidth:200,maxWidth:i.maxCodeWidth,handles:"e",create:function(e,t){d("#nodeWizardEval").width(i.dockedWindowWidth-i.maxCodeWidth-12),i.$el.find(".resultArea").width(i.dockedWindowWidth-i.maxCodeWidth-12)},resize:function(e,t){d("#nodeWizardEval").width(i.dockedWindowWidth-i.$el.find(".codeArea").width()-12),i.$el.find(".resultArea").width(i.dockedWindowWidth-i.$el.find(".codeArea").width()-12)},stop:function(e,t){d("#nodeWizardEval").width(i.dockedWindowWidth-i.$el.find(".codeArea").width()-12),i.$el.find(".resultArea").width(i.dockedWindowWidth-i.$el.find(".codeArea").width()-12),d.cookie("resultAreaWidth",i.dockedWindowWidth-i.$el.find(".codeArea").width()-12,{expires:365})}}),d(".nodeWizardTab").trigger("updateSizes")}var a={maxHeight:800,maxWidth:1920,minHeight:100,minWidth:1024};e.hasClass("left")?a.handles="e":e.hasClass("right")?(a.handles="w",a.resize=function(e,i){i.helper.css("left","")}):e.hasClass("top")?a.handles="s":e.hasClass("bottom")?(a.handles="n",a.resize=function(e,i){i.helper.css("top","")}):a.handles="all",a.resize=function(e,i){d(".dockInfluenceDiagramProperty").trigger("updateWidth")},e.resizable(a),d(".nodeWizardTab").trigger("updateSizes")},addKeyboardHandlers:function(e){},saveDockPosition:function(e,i){var t={zone:i,top:e.css("top"),left:e.css("left"),width:e.width(),height:e.height()};d.inArray("top",this.options.positions)>0||d.inArray("bottom",this.options.positions)>0?d.cookie("cubeplan_doc_pos_vertical",JSON.stringify(t),{expires:365}):d.cookie("cubeplan_doc_pos_horizontal",JSON.stringify(t),{expires:365})},setDockPosition:function(e){var i;if((i=d.inArray("top",this.options.positions)>0||d.inArray("bottom",this.options.positions)>0?d.cookie("cubeplan_doc_pos_vertical"):d.cookie("cubeplan_doc_pos_horizontal"))&&""!=i){var t=JSON.parse(i);if(t.zone){d(e).css({left:"",top:"",height:"",width:""}),d(e).addClass(t.zone).addClass("docked");var o=d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").parent().width();d(".mainTask.influence-diagram .dockInfluenceDiagramProperty").width(o-105)}else t.top+25>d(window).height()&&(t.top=d(window).height()-50),t.left+25>d(window).width()&&(t.left=d(window).width()-50),d(e).removeClass("docked").removeClass("left").removeClass("right").removeClass("top").removeClass("bottom"),d(e).css(t)}}})}.apply(i,a))||(e.exports=n)}).call(this,t(218),t(1))},2077:function(e,i,t){var o=t(690);e.exports=(o.default||o).template({compiler:[7,">= 4.0.0"],main:function(e,i,t,o,d){var a,n=null!=i?i:e.nullContext||{},s=t.helperMissing,r=e.escapeExpression;return"<div id='"+r("function"==typeof(a=null!=(a=t.id||(null!=i?i.id:i))?a:s)?a.call(n,{name:"id",hash:{},data:d}):a)+"' class='box box-color satblue dock dockItem docked "+r("function"==typeof(a=null!=(a=t.className||(null!=i?i.className:i))?a:s)?a.call(n,{name:"className",hash:{},data:d}):a)+" box-small'>\n\n  <div class='box-title header dragger'>\n    <div class='dockCommandBtns'>\n      <i class='fa fa-arrows dockMove dragger'></i>\n      <i class='fa fa-minus dockMinimize' data-action='minimize'></i>\n      <i class='far fa-square dockMaximize' data-action='maximize'></i>\n    </div>\n    <h3 class='nodeTextTitle'>"+r("function"==typeof(a=null!=(a=t.title||(null!=i?i.title:i))?a:s)?a.call(n,{name:"title",hash:{},data:d}):a)+"</h3>\n\n  </div>\n\n  <div class='box-content dock-container'>\n\n  </div>\n</div>"},useData:!0})}}]);