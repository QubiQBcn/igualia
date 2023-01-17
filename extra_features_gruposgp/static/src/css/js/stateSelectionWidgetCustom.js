odoo.define('extra_features_gruposgp.stateSelectionWidgetCustom', function(require) {
    "use strict";
    
    var core = require('web.core');
    var qweb = core.qweb;
    
    var basic_fields = require('web.basic_fields');
    
    let log = console.log; // DeBUG
    basic_fields.StateSelectionWidget.include({
    
        /**
         * WARN: Ovverride!!! Original DIR:  web\static\src\js\fields\basic_fields.js
         * Original DOCS: 
         * Prepares the state values to be rendered using the FormSelection.Items template.
         *
         * @private
         */
        _prepareDropdownValues: function () {
            var self = this;
            var _data = [];
            var current_stage_id = self.recordData.stage_id && self.recordData.stage_id[0];
            var stage_data = {
                id: current_stage_id,
                legend_normal: this.recordData.legend_normal || this.recordData.project_legend_normal || undefined,
                legend_processed: this.recordData.legend_processed || this.recordData.project_legend_normal || undefined,
                legend_blocked : this.recordData.legend_blocked || this.recordData.project_legend_normal || undefined,
                legend_done: this.recordData.legend_done || this.recordData.project_legend_normal || undefined,
            };
            console.log("stage_data", stage_data);
            _.map(this.field.selection || [], function (selection_item) {
                var value = {
                    'name': selection_item[0],
                    'tooltip': selection_item[1],
                };
                if (selection_item[0] === 'normal') {
                    value.state_name = stage_data.legend_normal ? stage_data.legend_normal : selection_item[1];
                } 
                // OVERRIDEN
                else if (selection_item[0] == 'processed') {
                    value.state_class = 'o_status_yellow';
                    value.state_name = stage_data.legend_processed ? stage_data.legend_processed : selection_item[1];
                } 
                // -------------------------
                else if (selection_item[0] === 'done') {
                    value.state_class = 'o_status_green';
                    value.state_name = stage_data.legend_done ? stage_data.legend_done : selection_item[1];
                } else {
                    value.state_class = 'o_status_red';
                    value.state_name = stage_data.legend_blocked ? stage_data.legend_blocked : selection_item[1];
                }
                _data.push(value);
            });
            return _data;
        },
    
        /**     
         * WARN: Ovverride!!! Original DIR:  web\static\src\js\fields\basic_fields.js
         * Original DOCS: 
         * This widget uses the FormSelection template but needs to customize it a bit.
         *
         * @private
         * @override
         */
        _render: function () {
            var states = this._prepareDropdownValues();
            // Adapt "FormSelection"
            // Like priority, default on the first possible value if no value is given.
            var currentState = _.findWhere(states, {name: this.value}) || states[0];
            this.$('.o_status')
                .removeClass('o_status_red o_status_green o_status_yellow')  // Modified
                .addClass(currentState.state_class)
                .prop('special_click', true)
                .parent().attr('title', currentState.state_name)
                .attr('aria-label', this.string + ": " + currentState.state_name);
    
            // Render "FormSelection.Items" and move it into "FormSelection"
            var $items = $(qweb.render('FormSelection.items', {
                states: _.without(states, currentState)
            }));
            var $dropdown = this.$('.dropdown-menu');
            $dropdown.children().remove(); // remove old items
            $items.appendTo($dropdown);
    
            // Disable edition if the field is readonly
            var isReadonly = this.record.evalModifiers(this.attrs.modifiers).readonly;
            this.$('a[data-toggle=dropdown]').toggleClass('disabled', isReadonly || false);
        },
    
    
    });
    
    
    return;
    
    });