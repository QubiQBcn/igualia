odoo.define('extra_features_gruposgp.stateOne2ManyWidget', function(require) {
    "use strict";
    
    
    var core = require('web.core');
    var field_registry = require('web.field_registry');
    var qweb = core.qweb;
    var relationalFields = require('web.relational_fields');
    
    var StateOne2ManyWidget = relationalFields.FieldMany2ManyTags.extend({
        template: 'FormStateO2ManySelection',
         events: {
            'click .dropdown-item': '_setValues',
        },
    
        //--------------------------------------------------------------------------
        // Public
        //--------------------------------------------------------------------------
    
        /**
         * Returns the drop down button.
         *
         * @override
         */
        getFocusableElement: function () {
            return this.$("a[data-toggle='dropdown']");
        },
    
    
        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------
    
        /**
         * Prepares the state values to be rendered using the FormSelection.Items template.
         *
         * @private
         */
        _prepareOne2ManyValues: function() {
          let self = this;
          let currentStageId = self.recordData.stage_id && self.recordData.stage_id;
          let statgesIds = this.value.data;
          var stages = [];
          _.each(statgesIds, function (stage_id) {
              if (stage_id.data.id != currentStageId.data.id) { // coercion intended
                      let value = {
                      'id': stage_id.data.id,
                      'name': stage_id.data.display_name,
                      'dataId': stage_id.id
                  };
                  stages.push(value);
              }
          })
          return [currentStageId, stages];
        },
    
        /**
         * This widget uses the FormStateO2ManySelection.items template but needs to customize it a bit.
         *
         * @private
         * @override
         */
        _render: function () {
            let [currentStageId, stages] = this._prepareOne2ManyValues();
            let $stages = $(qweb.render("FormStateO2ManySelection.items", {
                currentStageId: currentStageId,
                stages: stages
            }));
            var $dropdown = this.$('.dropdown-menu');
            // $dropdown.children().remove(); // remove old items
            $stages.appendTo($dropdown);
    
        },
        /**
         *
         * @overwrite
         */
        _setValues: function (event) {
            event.stopPropagation();
            let self = this;
            let target = event.target;
            let target_id = target.dataset.id;
            let stages = self.value.data;
            let new_record = undefined;
            stages.some( (el) => {
                 let el_id = el.data.id;
                 let match = el_id == target_id;  // coercion intended
                 if (match) {
                     new_record = el;
                     return true;
                 } else {
                     return false;
                 }
    
            });
            // TODO/IMP, learn how to do it directly with the JS Script Framework. Despite finally, we always need
            // to call the Server Python side, the Odoo JS Framework should use other lower method.
            // For the momemnt is ok though
            if (new_record) {
                self._rpc({
                    model: self.model,
                    method: 'write',
                    args: [self.res_id, {'stage_id': new_record.data.id} ],
                })
                .then(function() {
                   return self.trigger_up('reload');
                });
            }
        },
    });
    
    field_registry.add('one2many_state_selection', StateOne2ManyWidget);
    return { StateOne2ManyWidget: StateOne2ManyWidget };
    });