extra_features_gruposgp
==============================


Author
------

* [iTundra.com](https://www.tundra-group.com/itundra)
* Date: 19th May - 2021


-----------------------------------------------------------------------------------------------------



Package Version
---------------

* 13.0.2.14

-----------------------------------------------------------------------------------------------------

Change Versions & Extra Features
--------------------------------
### Change Log 21/03/2021 | Blaise De Carvalho | TASK: 10.40 | 13.0.2.30--> 13.0.2.31
#### UPDATE
Add the fields num_employees and deal to the tree view as hiden.
res_partner_views.xml --> add new view res_partner_tree_view_extra_features that inherit from base.view_partner_tree
add the two new fields 


### Change Log 21/03/2021 | Blaise De Carvalho | TASK: 10.40 | 13.0.2.29--> 13.0.2.30
Add two fields to res_partner.`py --> num_employees and deal,both are integer fields.
Added them to the form view. Invisible if is_company is not true


#### UPDATE
Sale_views.xml --> change domain for user_id. We want the selection field is related to the groups with id 11 or 8


### Change Log 10/03/2021 | Blaise De Carvalho | TASK: 10.39 | 13.0.2.28--> 13.0.2.29


#### UPDATE
Sale_views.xml --> change domain for user_id. We want the selection field is related to the groups with id 11 or 8

### Change Log 10/03/2021 | Blaise De Carvalho | TASK: 10.39 | 13.0.2.28--> 13.0.2.29


#### UPDATE
Sale_views.xml --> Change user_id field attribute : {'no_create': True, 'no_create_edit':True}


### Change Log 10/03/2021 | Blaise De Carvalho | TASK: 10.38 | 13.0.2.27--> 13.0.2.28


#### UPDATE
Add agent_id to sale.view_quotation_tree



 
### Change Log 22/12/2021 | Federico Bau | TASK: 10.32 | 13.0.2.26--> 13.0.2.27


#### FIX

Removed field `check_list_project_id` in form view of task if user is does not have `project.group_project_manager`
access right. 

* **project.task**
  * Field: `check_list_project_id` Added group `groups="project.group_project_manager"` to field 

### Change Log 16/12/2021 | Federico Bau | TASK: 10.32 | 13.0.2.25--> 13.0.2.26

#### FIX 

* All event fields are required in the Event Form. 

* **event.registration**
  * `extra_features_gruposgp_registration_attendee_details`


### Change Log 15/12/2021 | Federico Bau | TASK: 10.30 |13.0.2.24 --> 13.0.2.25

### FIX / HACK HACK_ACCESS_RIGHTS

User of group Project / User can't change the Project Stage because are
owned by the project. An HACK in order to 'upgrade' the user has been done in method 'write'

* **project.project**
  * Method: `write`

Full explanation

>>>   HACK_ACCESS_RIGHTS HACK: Use this fields in order to 'upgrade' the user (namely it should be the project.group_project_user so the
User of the Project with most minimal entry. THis is because the fields in FIELD_TO_UPGRADE are
use by Project user as well however the project.project fileds are readonly for the Project Users.
I tried to add 'groups' to the fields however it seems that it doesnt have affect
because the fields are already created. And manually add the groups into the fields with a scripts seems
overkill (and may cause issue to the DB).
Right now, the fields are alredy created since a while in production and a delete and re-create them will cause a data loss.
What was supposed to do since the beginning (if it was known that project.group_project_user needed to change
the project fields listed in FIELD_TO_UPGRADE as well) was to create a separeate common table or to add groups='project.group_project_user' in
this fields (however not sure if this would work neither, hence first solution is the best

### Change Log 07/12/2021 | Federico Bau | TASK: 10.30 | 13.0.2.23 --> 13.0.2.24

#### UPD

Field `title, company_id` in checklist tree set to optional = `hide`

* **project.checklist** 
  * View: `project_checklist__tree_view`


### Change Log 15/11/2021 | Federico Bau | TASK: 10.29 | 13.0.2.22--> 13.0.2.23

#### ADD

1.- In the tree view of the checklist, it must be possible to filter by Responsible and Responsible for support that the Projects have
2.- Group the projects`employee_id_manager, user_id_hr`

* **project.checklist**
  * New fields: `employee_id_manager, user_id_hr` related to project
  * New fields: `employee_id_manager_groupby, user_id_hr_groupby, group_by_trigger` fields
  * Added in view `project_checklist__search_view` as fields and groubby filters
  
Note for the 3 computed fields.
#### **HACK**

>  Odoo does not support Group by related m2o fields and by m2m fields or related m2m fields
  This simple hack uses instead Char type computed field, collecting name of the related fields and
  smash them together into a unique string. In same cases, it may be pretty ugly (where many related fields withb many
  name are. That's why we first convert the name into a set, in order to remove at least the duplicates.
  NOTE: very important is the '_compute_trigger_groupby' function which is trigger by the field, which can by of any
  type really but an Integer was choose as representitive of a True Value. It must be present in the View (Tree, kanban etc..)
  What it does is computing every time, as then triggers the real group by funcitin. That's because, the group by
  fields need to be stored, but if not trigger of the depends function are called, as well as older records, the depends
  function won't be called.

### Change Log 11/11/2021 | Federico Bau | TASK: 10.28 | 13.0.2.21 --> 13.0.2.22

#### FIX 

* **project.checklist.line**
  * Change description to --> `'Project Checklist Line'`

* **project.checklist.line, project.checklist**
  * Change Security level from Project Administrator to Project User (`group_project_manager` --> `group_project_user`)

### Change Log 28/10/2021 | Federico Bau | 13.0.2.19 --> 13.0.2.21
####TASK 10.26
#### FIX

Created a custom widget for Project Kanban view in order to quick change the stage_id

* **JS Widget: `StateOne2ManyWidget`

### Change Log 20/10/2021 | Federico Bau | 13.0.2.19 --> 13.0.2.20

#### ADD


Project uses the same Task stages instead set that are related for each project. 
The stage_id is then displayed as progress bar in the View form and tree form and as a colored ball in the Kanban View 
By default, the project will have the first stage_id as is deault state. 


* **project.project.type**
  * New Model, which is a copy of `project.task.type` but for the projects, has slightyl less functionallity (kanban state are not used.) 

* **project.task.type**
  * Function create and write extended, detects the first project_type for each project and assign it to the project.stage_id 
  if none is set. 
  * New Fields: `color`
* **project.project**
  * New field: 'stage_id'
* **project.task**
  * New Fields: `project_stage_id` related to: `project_id.stage_id`
  
### Change Log 20/10/2021 | Federico Bau | 13.0.2.18 --> 13.0.2.19

#### ADD

* **project.project**
  * Added tracking to fields: `task_user_id_hr, task_user_id_no_limit`
  * Added tracking for `update_task_responsable` method (in customize)
* **project.task**
   * Added tracking to fields: `user_id_hr`
* **mail.message.subtype**
  * Added 3 new data records: `project_update_task_user_method, project_update_employee_manager, project_update_project_task_user`


### Change Log 11/10/2021 | Federico Bau | 13.0.2.17 -> 13.0.2.18

* **project.project, project.task**
  * New field: `employee_id_manager m2o -> hr.employee`
  * Function: `update_task_responsable` (module `customize' ) adds the `employee_id_manager` user_id_no_limit.partner_id to the followers

### Change Log 7/10/2021 | Federico Bau | 13.0.2.16--> 13.0.2.17

* **project.task** `user_id_hr` from many2one -> many2many

### Change Log 6th October - 2021 | Federico Bau | 13.0.2.15 -> 13.0.2.16

#### UPD

**project.task**
  * Project Task default view change from kanban to tree
    * Act_window: `open_view_task_list_kanban,open_view_task_list_tree,project.act_project_project_2_project_task_all,project.action_view_task`
  * Added tree view editable
  * Added to tree view button to open task form
    * View: `view_task_tree2_custom`

### Change Log 5th October - 2021 | Federico Bau | 13.0.2.14 -> 13.0.2.15

### FIX / BUG

When using res.partner filter (kanban or tree view) and use 'sale_order_ids' is set it gives your wrong 
contacts sometimes. 

This is because, the field used to show the Sales count (res.partner.sale_order_count) don't shows the archieved 
sale order, same with res.partnersale_order_ids. However when using the filter somehow it detects that the sale_order_ids
is not False hence, showing up partners with sale count to 0 

Fixed by adding a filter sale_order_count_filter to `base.view_res_partner_filter` with a domain ('sale_order_ids.active', '=', True)
fix it.

* **res.partner**
  * View: `extra_features_gruposgp_view_res_partner_filter` (`base.view_res_partner_filter`)

### Change Log 29nd September - 2021 | Federico Bau | 13.0.2.13 -> 13.0.2.14

* When creating a Partner Checklist, all the olrder project of the Partner's company will get the Cheklist as well.
* Added filters to project_checklist__search_view : "Question title, Find Comment, Question Document Date to quick filter the
checklist line inside the Project Checklist view

### Change Log 23nd September - 2021 | Federico Bau | 13.0.2.12--> 13.0.2.13

* **project.project**
  * Fields `user_id_hr, task_user_id_hr` became Many2many.
  * fixed function `update_task_responsable`
  * Function `get_main_project_user_hr_id` will determine which is the main Project's user_id


### Change Log 22nd September - 2021 | Federico Bau | 13.0.2.11--> 13.0.2.12

The `project.checklist` is created based on the Partner and not the Projects, hence there should be on Checklist
for each Partner and many Projects related to the checklist, these are the main specs:

* When creating a project if contact doesn't have a checklist it will crete, else will use the one created.
* A new button is added to the partner form in order to create a new checklist
* Checklist are created for each contact, the project will be assign depending on the Contact checklist and not the
business'contact (contact's parent_id) so if the contact has not the checklist the checklist is not assigned even if the
parent contact has it.

* **project.checklist**
  * Function `create_new_checklist` will create a checklist and relate it to the partner, if a project is 
  present, it will add the project to it
* **project.project**
  * Field: `check_list_id` 
* **res.partner**
  * field `has_checklist` will compute whether the partner has the checklist or not, is only used to display an action
  buttton in the res.partner form -> `action_create_checklist` which will assign a new check list for the partner
  

### Change Log 16 September - 2021 | Federico Bau | 13.0.0.2.10 --> 13.0.0.2.11
**Task: 10.19**

* **Report -> web.external_layout_standard** Overwritten in order to modify the Company address
* **Report -> account.report_invoice_document** Overwritten, removed o.invoice_origin and replaced with o.invoice_payment_term_id

### Change Log 16 September - 2021 | Federico Bau | 13.0.0.2.9 --> 13.0.0.2.10
**Task: 10.15**

* **project.checklist**
  * Added Root Menu to Sales after Reporting
  * Added Security Group --> `sales_team.group_sale_salesman`

### Change Log 18th August - 2021 | Federico Bau | 13.0.0.2.8--> 13.0.0.2.9
**Task: 10.18**

Report Template Changed, added the following images into the Report document footer, changes are made only for the 
company 'IGUALIA - GRUPO SGP'. In order to check which company the change it applies, I currently use the company VAT
which is ESB63745848

Logo 1: https://erp.igualia.net/web/image/13418411/1.jpg

Logo 2: https://erp.igualia.net/web/image/13418412/2.jpg

* **web.external_layout_clean** : 
  * NOTE: The is code is higly dipendent on the Grupo SGB requirements, hence if any data used as conditional statement
is changed, this template must be changed as well or obviously it won't work.

### Change Log 18th August - 2021 | Federico Bau | 13.0.0.2.7--> 13.0.0.2.8
**Task: 10.17**

### UPD

* **project.checklist**: 
  * Field: `sale_agent_id` Added args: domain=[("agent", "=", True)], store=True, readonly=False 
  * Description changed: `Project CheckList`

### Change Log 28th JuLY - 2021 | Federico Bau | 13.0.0.2.6 --> 13.0.0.2.7
**Task: 10.17**

Added FIelds to Sale Report and Project report

* **project.profitability.report** New fields: `user_id_hr`, `kanban_state`
* **sale.report** New Fields: New fields: `days_to_confirm,invoice_status `


### Change Log 27th JuLY - 2021 | Federico Bau | 13.0.0.0.2.2 --> 13.0.0.2.4 --> 13.0.0.2.5  --> 13.0.0.2.6
**Task: 10.15** 

### UPD

  **Added filters to `project.checklist` in search view ' project_checklist__search_view' in order to get questions
  with yes / no answer or no answer**

* **project.checklist.line**, **project.checklist**
  * Added to field `selection` --> `no_answer` 
  
-------------------------------
  **ADDED KANBAN STATE TO PROJECT PROJECT --> legend_processed (Tramitado)**

* **project.project**
  * New field: `legend_processed`
  * New Element added to field: `kanban_state` selection + `processed`
* Overwritten widget `StateSelectionWidget` with JS wich handles the Kanban state. 
* Added CSS stylesheet with new class `o_status_yellow` with yellow color for the  `legend_processed` kanban state.
-------------------------------

* **project.checklist**
  * project_id --> readonly
-------------------------------
* **project.task**
  * Added fields: `check_list_id` related to -> `project_id.check_list_id
  * Added fields: `    check_list_name, check_list_project_id, check_list_partner_id, check_list_compa  check_list_phone,  check_list_mobile, check_list_stre check_list_rlt_company, check_list_rlt_all_working_place, check_list_sale_agent_id , check_list_equality_commission, check_list_working_people_number, check_list_work_place, check_list_agreement, check_list_line = fields.One2many(related='check_list_id.check_list_line', readonly=False)`   related to -> `project.task.check_list_id`
  
### Change Log 22th JuLY - 2021 | Federico Bau | 13.0.0.0.2.2 --> 13.0.0.2.3
**Task: 10.15** 

======================== < ADD > ========================

Added Project CheckList 

** project.checklist, project.checklist.line


### Change Log 29th June - 2021 | Federico Bau | 13.0.0.0.9 --> 13.0.0.0.2.2
**Task: 10.12**  

======================== < FIX > ========================

* Duplicate Email addres can't be registered Twice in the Event 

======================== < ADD > ========================

* depends: `website_event`

* **WebsiteEventController**
    * Function: registration_confirm | It will create a new Contact if the logged User is not registered or is an internal user

* Template **website_event.registration_attendee_details** Added:  `Company (comment)  Job Title (function)`

### Change Log 25th June - 2021 | Federico Bau | 13.0.0.0.8 --> N/A
**Task: 10.11**  

======================== < FIX > ========================

* **res.partner**
    * View: `base.view_partner_form`
    * If Partner without `sales_team.group_sale_salesman` Group would thrown an error because xpath couldn't find some fields
    

### Change Log 21th June - 2021 | Federico Bau | 13.0.0.0.7 --> 13.0.0.0.8
**Task: 10.10**  

======================== < ADD > ========================

* **res.partner**
Switch these 2 field type
    * agent_ids -> Many2one
    * creditor_id_many2one_ids -> One2many
### Change Log 21th June - 2021 | Federico Bau | 13.0.0.0.5 --> 13.0.0.0.7
**Task: 10.10**      


======================== < ADD > ========================

* **depends**: account
* **res.partner** View: `view_partner_form` + `customer_rank,supplier_rank

### Change Log 4th June - 2021 | Federico Bau | 13.0.0.0.5 --> 13.0.0.0.6
### 10.9


      ======================== < ADD > ========================
      
* depends: `sale_commission`

* **sale.order**
> New Field ``agent_id`` Many2one res.partner 
> Adds automatically agent_id if `res.partner` has an Agent_id

* **res.partner**
> New Field ``agent_ids`` One2many res.partner ->  ``creditor_id_many2one`` (overrifes the on from sale_commission Many2many)
> New Field ``creditor_id_many2one`` Many2one res.partner 
      
  
### Change Log 4th June - 2021 | Federico Bau | V13.0.0.0.3 --> 13.0.0.0.5
### 10.8

* **sale.order**
>  Views: sale.view_quotation_tree,sale.view_order_tree:
> Added order_line as many2many_tags widget


### Change Log 4th June - 2021 | Federico Bau | V13.0.0.0.1 --> 13.0.0.0.2
**Task: 10.2, 10,3**

      ======================== < ADD > ========================
      
* **depends**: base, sale, contacts
* **sale.order**
    * View: `view_order_form_inherit_extra_features (sale.view_order_form)`, fields date_order changed groups sales_team.group_sale_salesman
    * View: `view_quotation_tree_with_onboarding_extra_features (sale.view_quotation_tree)` Added field date_order

* New DB Model: **res.partner.company.type** 

* **res.partner**
    * Fields Many2one: `contact_company_type` related to --> res.partner.company.type
    * Added fields `contact_company_type` to `view_partner_form_extra_features (base.view_partner_form)`

### First Commit 20th May - 2021


      ======================== < ADD > ========================

* **project.project**
    * Added 3 Label Stages (as for project.task) plus Views in Form & Kanban


----------------------------------------------------------------
[SUBIDA CARPETA] SAT CRM

        >>> Modulo: extra_features_satcrm
        >>> Version: 13.0.0.0.1


-----------------------------------------------------------------------------------------------------


Requirements
------------

### Oddo's native Modules

* Project

### 3rd Party Modules

* N/A

### Python 3rd Party Packages

* N/A

-----------------------------------------------------------------------------------------------------


Additional Notes
----------------