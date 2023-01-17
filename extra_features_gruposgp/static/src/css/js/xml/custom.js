var log = console.log;

odoo.define('extra_features_gruposgp.website_event_custom', function (require) {
    "use strict";
var ajax = require('web.ajax');
var core = require('web.core');
var Widget = require('web.Widget');
var publicWidget = require('web.public.widget');
var websiteEvent = require('website_event.website_event');
log("publicWidget", publicWidget);
log("publicWidget", publicWidget.registry);


var EventRegistrationFormCheckEmailDuplicate = Widget.extend({
    events: {
        'click #attendee_detailsSubmit': '_onAttendeeBtnClick',
    },
    
    start: function () {
        var self = this;

        var res = this._super.apply(this.arguments).then(function () {
            $('#modal_attendees_registration')             
                .click(function (ev) {
                    log("CLICKED", ev)
                
                });
        });
        return res;
    
    },

    /**
     * @private
     * @param {Event} ev
     */
    _onAttendeeBtnClick: function (ev) {
        var $btn = $(ev.currentTarget);
        log("Butoon Clicked", $btn);
        alert("Hey Many");
    },

});

publicWidget.registry.EventRegistrationFormCheckEmailDuplicate = publicWidget.Widget.extend({
    selector: '#registration_form',  

    /**
     * @override
     */
    start: function () {
        log("Hello World");
        log("This, el", this.$el);
        var def = this._super.apply(this, arguments);
        this.instance = new EventRegistrationFormCheckEmailDuplicate(this);
        return Promise.all([def, this.instance.attachTo(this.$el)]);
    },

    destroy: function () {
        this.instance.setElement(null);
        this._super.apply(this, arguments);
        this.instance.setElement(this.$el);
    },
})

return EventRegistrationFormCheckEmailDuplicate;

});