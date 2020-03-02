/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[75],{1320:function(t,i,e){"use strict";(function(o,n){var s;void 0===(s=function(){return o.View.extend({el:"body",pointers:[],toolbars:[],currentSelection:void 0,currentNodetoMoveIn:void 0,rulesContainer:void 0,inJiggle:void 0,moveTimeOut:-1,clearSelection:function(){this.ensurePointers([]),this.currentSelection=null,this.$el.trigger("refreshStage")},selectNodes:function(t,i){this.ensurePointers(t),this.animatePointers(t,0,i),this.currentSelection=t},setCurrentSelection:function(t){this.currentSelection=t},addSelectedNodes:function(t){this.currentSelection||(this.currentSelection=[]);for(var i=t.length-1;i>=0;i--){var e=this.currentSelection.indexOf(t[i]);e>=0&&(t.splice(i,1),this.currentSelection.splice(e,1),this.removePointerFromBoxPosition(e))}if(t.length>0){var o=this.currentSelection.length;this.currentSelection=this.currentSelection.concat(t),this.ensurePointers(this.currentSelection),this.animatePointers(t,o)}this.detectMultiselect()},setCurrentSelections:function(t){this.currentSelection||(this.currentSelection=[]),t.length>0&&(this.currentSelection=this.currentSelection.concat(t))},refreshAll:function(){this.currentSelection&&this.animatePointers(this.currentSelection,0,0)},removePointerFromBoxPosition:function(t){var i=this.toolbars[t];this.options.stage.removeChild(i),this.toolbars.splice(t,1);for(var e=t*=4;e<this.pointers.length&&e<t+4;e++)i=this.pointers[e],this.options.stage.removeChild(i);this.pointers.splice(t,4),this.$el.trigger("refreshStage")},ensurePointers:function(t){var i=4*t.length;if(this.pointers.length>i){for(;this.pointers.length>i;){var e=this.pointers.pop();this.options.stage.removeChild(e)}for(;this.toolbars.length>i/4;){e=this.toolbars.pop();this.options.stage.removeChild(e)}this.$el.trigger("refreshStage")}else{var o=i-this.pointers.length;this.createPointers(o),this.createToolbars(o/4)}},createPointers:function(t){for(var i=0;i<t;i++){var e=new PIXI.Container,o=new PIXI.Graphics;e.addChild(o),this.drawPointer(e,8026797),e.position.x=Math.floor(Math.random()*this.options.stage.width),e.position.y=Math.floor(Math.random()*this.options.stage.height),this.options.stage.addChild(e),this.pointers.push(e),this.registerPointerEvents(e)}},createToolbars:function(t){for(var i=0;i<t;i++){var o=new PIXI.Container,n=PIXI.Texture.fromImage(e(1991)),s=new PIXI.Sprite(n);o.addChild(s),this.addMoveEvents(s),o.position.x=Math.floor(Math.random()*this.options.stage.width),o.position.y=Math.floor(Math.random()*this.options.stage.height),this.options.stage.addChild(o),this.toolbars.push(o)}},detectMultiselect:function(){if(this.pointers&&this.pointers.length>3){for(var t=0;t<this.pointers.length-4;t++)this.drawPointer(this.pointers[t],16708060);this.drawPointer(this.pointers[this.pointers.length-1],16569495),this.drawPointer(this.pointers[this.pointers.length-2],16569495),this.drawPointer(this.pointers[this.pointers.length-3],16569495),this.drawPointer(this.pointers[this.pointers.length-4],16569495)}},drawPointer:function(t,i){var e=t.children[0];e.beginFill(i),e.lineStyle(.5,8145924,1),e.drawRect(-4,-4,8,8),e.endFill()},animatePointers:function(t,i,e){this.detectMultiselect();var o=this,s="Cubic.easeOut",r=[0,1,2,3];i||(i=0),0===e&&(e=1e-5),e||(e=.4),e=1e-5;for(var a=0;a<t.length;a++){this.shuffleArray(r);var h=a+i,l=4*(a+i)+r[0],c=4*(a+i)+r[1],d=4*(a+i)+r[2],p=4*(a+i)+r[3],u=this.toolbars[h];u.relatedBox=t[a],TweenMax.set(u.position,{x:parseInt(t[a].position.x+t[a].width/2)-8,y:t[a].position.y-4-18});new TweenMax(this.pointers[l].position,e,{x:t[a].position.x-4,y:t[a].position.y-4,ease:s}),new TweenMax(this.pointers[c].position,e,{x:t[a].position.x+t[a].width+4,y:t[a].position.y-4,ease:s}),new TweenMax(this.pointers[d].position,e,{x:t[a].position.x-4,y:t[a].position.y+t[a].height+4,ease:s}),new TweenMax(this.pointers[p].position,e,n.extend({x:t[a].position.x+t[a].width+4,y:t[a].position.y+t[a].height+4,ease:s,onComplete:function(){new TweenMax(n.extend({alpha:1},o.options.animationEngineOptions))}},this.options.animationEngineOptions));this.pointers[l].resizeData="1",this.pointers[c].resizeData="2",this.pointers[d].resizeData="3",this.pointers[p].resizeData="4";var g=n.uuid();this.pointers[l].uid=this.pointers[c].uid=this.pointers[d].uid=this.pointers[p].uid=g}},addMoveEvents:function(t){var i=this;t.interactive=!0,t.mousedown=t.touchstart=function(t){var e=t.data;e.originalEvent.stopImmediatePropagation(),e.originalEvent.stopPropagation(),e.originalEvent.preventDefault(),t.stopPropagation(),this.data=e,this.deltaX=this.data.getLocalPosition(this.parent.parent).x-this.parent.relatedBox.position.x,this.deltaY=this.data.getLocalPosition(this.parent.parent).y-this.parent.relatedBox.position.y,this.deltaToolbarX=this.data.getLocalPosition(this.parent).x,this.deltaToolbarY=this.data.getLocalPosition(this.parent).y,this.dragging=!0,i.hideOthers(this.parent)},t.mouseup=t.mouseupoutside=t.touchend=t.touchendoutside=function(t){t.stopPropagation(),this.dragging=!1,this.data=null,this.parent.relatedBox=null,i.showAll(),i.animatePointers(i.currentSelection,void 0,0),i.setNodesPosition(),i.hideAlignRules()},t.mousemove=t.touchmove=function(t){if(this.dragging){var e=this.data.getLocalPosition(this.parent.parent),o={x:this.parent.relatedBox.position.x,y:this.parent.relatedBox.position.y};this.parent.relatedBox.position.x=e.x-this.deltaX,this.parent.relatedBox.position.y=e.y-this.deltaY,o.x=o.x-this.parent.relatedBox.position.x,o.y=o.y-this.parent.relatedBox.position.y,this.parent.position.x=e.x-this.deltaToolbarX,this.parent.position.y=e.y-this.deltaToolbarY,i.updateOtherBox(this.parent.relatedBox,o),i.checkforMoveToModule(this.parent),i.showAlignRules(t.data.originalEvent.ctrlKey),i.$el.trigger("refreshArrows")}}},checkforMoveToModule:function(t){this.currentNodetoMoveIn=null;var i=this;n.each(this.options.stage.children,function(e,o){if(o&&o.nodeData&&t!=o&&("module"==o.nodeData.nodeClass||"module"==o.nodeData.originalClass)){if(new PIXI.Rectangle(o.position.x,o.position.y,o.width,o.height).contains(t.position.x,t.position.y))return i.currentNodetoMoveIn=o.nodeData.id,i.jiggle(o),!1;i.stopJiggle(o)}else i.stopJiggle(o)}),i=null},hideOthers:function(t){this.hideAll(),t.visible=!0},hideAll:function(){this.pointers&&this.pointers.length>0&&n.each(this.pointers,function(t,i){i.visible=!1}),this.toolbars&&this.toolbars.length>0&&n.each(this.toolbars,function(t,i){i.visible=!1})},showAll:function(){this.pointers&&this.pointers.length>0&&n.each(this.pointers,function(t,i){i.visible=!0}),this.toolbars&&this.toolbars.length>0&&n.each(this.toolbars,function(t,i){i.visible=!0})},updateOtherBox:function(t,i){n.each(this.currentSelection,function(e,o){o!=t&&(o.position.x-=i.x,o.position.y-=i.y)})},registerStageEvents:function(t){},registerPointerEvents:function(t){var i=this;t.interactive=!0,t.mousedown=t.touchstart=function(t){var e=t.data;e.originalEvent.stopImmediatePropagation(),e.originalEvent.stopPropagation(),e.originalEvent.preventDefault(),t.stopPropagation(),this.dragging=!0,this.data=e,this.deltaX=this.data.getLocalPosition(this.parent).x-this.position.x,this.deltaY=this.data.getLocalPosition(this.parent).y-this.position.y,i.hideOthers(this)},t.mouseup=t.mouseupoutside=t.touchend=t.touchendoutside=function(t){t.stopPropagation(),this.dragging=!1,this.data=null,i.showAll(),i.animatePointers(i.currentSelection,void 0,0);var e=[];n.each(i.currentSelection,function(t,i){var o={id:i.nodeData.id,x:i.position.x,y:i.position.y,w:i.nodeData.w,h:i.nodeData.h};e.push(o)}),i.$el.trigger("setNodeSize",[e])},t.mousemove=t.touchmove=function(e){if(this.dragging){var o=e.data.originalEvent.shiftKey,s=this.data.getLocalPosition(this.parent),r=!0,a=!0;n.each(i.currentSelection,function(t,i){i.nodeData.w<=i.minWidth&&(r=!1),i.nodeData.h<=i.minHeight&&(a=!1)});var h=s.x-this.deltaX-this.position.x,l=s.y-this.deltaY-this.position.y,c=i.updateSizeOfAllBoxes(t,h,l,r,a,o);if(0==c[0])this.position.x=s.x-this.deltaX;else{var d=i.getBoxFromPointer(t);switch(t.resizeData){case"2":case"4":this.position.x=d.position.x+d.width+4;break;case"1":case"3":this.position.x=d.position.x-4}}if(0==c[1])this.position.y=s.y-this.deltaY;else{d=i.getBoxFromPointer(t);switch(t.resizeData){case"1":case"2":this.position.y=d.position.y-4;break;case"3":case"4":this.position.y=d.position.y+d.height+4}}i.$el.trigger("refreshArrows")}}},shuffleArray:function(t){for(var i,e,o=t.length;0!==o;)e=Math.floor(Math.random()*o),i=t[o-=1],t[o]=t[e],t[e]=i;return t},getBoxFromPointer:function(t){var i=this.pointers.indexOf(t),e=Math.floor(i/4);return this.currentSelection[e]},updateSizeOfAllBoxes:function(t,i,e,o,s,r){var a=[0,0];return n.each(this.currentSelection,function(n,h){var l=0,c=0,d=0,p=0;switch(t.resizeData){case"1":l=i,c=e,d=-i,p=-e;break;case"2":l=0,c=e,d=i,p=-e;break;case"3":l=i,c=0,d=-i,p=+e;break;case"4":l=0,c=0,d=i,p=e}var u=h.nodeData.w+d>h.minWidth,g=h.nodeData.h+p>h.minHeight;r?(u&&o||d>0?(h.nodeData.w+=2*d,h.nodeData.x-=d):a[0]=1,g&&s||p>0?(h.nodeData.h+=2*p,h.nodeData.y-=p):a[1]=1):(u&&o||d>0?(h.nodeData.w+=d,h.nodeData.x+=l):a[0]=1,g&&s||p>0?(h.nodeData.h+=p,h.nodeData.y+=c):a[1]=1),h.refresh()}),a},stopJiggle:function(t){t&&t.stopJiggle&&t.stopJiggle(this.options.animationEngineOptions.onUpdate)},jiggle:function(t){t.jiggle(this.options.animationEngineOptions.onUpdate)},showAlignRules:function(t){if(this.rulesContainer||(this.rulesContainer=new PIXI.Graphics,this.options.stage.addChild(this.rulesContainer)),this.rulesContainer.clear(),this.currentSelection&&this.currentSelection.length>0){for(var i=[],e=[],o=[],n=0;n<this.currentSelection.length;n++)o.push(this.currentSelection[n].nodeData.id),i.push({center:this.currentSelection[n].position.x+this.currentSelection[n].width/2}),e.push({center:this.currentSelection[n].position.y+this.currentSelection[n].height/2});this.drawRules(i,e,o,t)}},drawRules:function(t,i,e,o){e||(e=[]);for(var n=this.options.stage.children,s=[],r=[],a=void 0,h=void 0,l=function(t){-1==s.indexOf(t)&&s.push(t)},c=function(t){-1==r.indexOf(t)&&r.push(t)},d=0;d<n.length;d++){var p=n[d];if(p.isNode&&-1==e.indexOf(p.nodeData.id)){for(var u,g,f=0;f<t.length;f++)(u=p.position.x+p.width/2)-10<t[f].center&&u+10>t[f].center&&(o||(a=u,this.currentSelection&&1==this.currentSelection.length&&(this.currentSelection[0].position.x=p.position.x+p.width/2-this.currentSelection[0].width/2)),l(u));for(f=0;f<i.length;f++)(g=p.position.y+p.height/2)-10<i[f].center&&g+10>i[f].center&&(o||(h=g,this.currentSelection&&1==this.currentSelection.length&&(this.currentSelection[0].position.y=p.position.y+p.height/2-this.currentSelection[0].height/2)),c(g))}}return this.drawRuleX(s,a),this.drawRuleY(r,h),{x:a,y:h,toEndX:!1,toEndY:!1}},drawRuleX:function(t,i){for(var e=0;e<t.length;e++)this.rulesContainer.lineStyle(.5,t[e]==i?16294687:14342874,.8),this.rulesContainer.moveTo(t[e],0),this.rulesContainer.lineTo(t[e],this.options.stage.height)},drawRuleY:function(t,i){for(var e=0;e<t.length;e++)this.rulesContainer.lineStyle(.5,t[e]==i?16294687:14342874,.8),this.rulesContainer.moveTo(0,t[e]),this.rulesContainer.lineTo(this.options.stage.width,t[e])},hideAlignRules:function(){this.rulesContainer&&(this.options.stage.removeChild(this.rulesContainer),this.rulesContainer=null)},setNodesPosition:function(){var t=this,i=[];n.each(this.currentSelection,function(e,o){var n={id:o.nodeData.id,x:o.position.x,y:o.position.y,moduleId:t.currentNodetoMoveIn};i.push(n)}),this.currentNodetoMoveIn?this.$el.trigger("moveNodesToModule",[i]):this.$el.trigger("setNodePosition",[i]),this.currentNodetoMoveIn=null},moveNodes:function(t){this.hideAll(),clearTimeout(this.moveTimeOut);var i={x:0,y:0};switch(t){case"up":i.y=1;break;case"down":i.y=-1;break;case"left":i.x=1;break;case"right":i.x=-1}this.updateOtherBox(void 0,i),this.showAlignRules(!0),this.$el.trigger("refreshArrows");var e=this;this.moveTimeOut=setTimeout(function(){e.refreshAll(),e.showAll(),e.setNodesPosition(),e.hideAlignRules(),e=null},510)}})}.apply(i,[]))||(t.exports=s)}).call(this,e(218),e(1))},1991:function(t,i){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAA1klEQVQ4jbVTuxHCMAzVMxMwRRgjBa0lZxaKpOCOcEcR7tiFT03BGMkUMEFEw3HEsQ0pUPn89N6zLBMlyloprZUyxZnFDphdDWAHYJllC3Rde/tZgNnVRLT5gPKUSLSYnTI7TXHMJMWUQGhYAPYA9j4+4jK7+ltUj6+vORGslRJA4zufz8fKazoQ0eoTU9XKGGPmvkPf9/eA8cMH3r0iRTP1CiLFIDWNAIpvYogbdfr7HiAEihSNqg6ih16GKPIXuq69ZtkCRJS/oO3lclpPjidSNN8G9gQYbU7CMrrSKwAAAABJRU5ErkJggg=="}}]);