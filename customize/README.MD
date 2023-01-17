xtra_features_gruposgp
==============================


Author
------

* [iTundra.com](https://www.tundra-group.com/itundra)
* Date: 19th May - 2021


-----------------------------------------------------------------------------------------------------


Package Version
---------------
 
* 13.0.0.1.2

-----------------------------------------------------------------------------------------------------

### Change Log 14/02/2021 | Blaise De Carvalho | Task: 10.37 |   13.0.0.1.40 -->  13.0.0.1.41

##### UPD

Added fields : four__notificacion_3er_requerimiento, four_contestacion_3er_requerimient, four__notificacion_4er_requerimiento
four_contestacion_4er_requerimiento, all related to Registro de Plan en REGCON

Change Registro de Plan en REGCON's form view style --> more columns, reduced field width to 70%

### Change Log 27/01/2021 | Federico Bau | Task: 10.36 |   13.0.0.1.38 -->  13.0.0.1.40

##### UPD

Added tracking to all `project.project` fields related to 'PROJECT TYPE BY CATEGORIES FIELDS'

### Change Log 27/01/2021 | Federico Bau | Task: 10.35 |   13.0.0.1.38 -->  13.0.0.1.39

##### UPD

Remove type_id field from project view task_timer_app `project.task.tree.custom`


### Change Log 10/12/2021 | Federico Bau | Task: 10.27 |   13.0.0.1.37 -->  13.0.0.1.38

#### ADD / IMP

Added the possibility to create activity for multiple Users

* **mail.activity**
  * New fields: `user_ids, is_main_activity, is_sub_activity, activity_main_id, activity_sub_ids`

### Change Log 10/12/2021 | Federico Bau | Task: 10.28 |   13.0.0.1.36 -->  13.0.0.1.37

#### UPD / ADD

* **project.project**
  * Added field `date_order` with widget `date` to all tree views of Project

* **project.task**
  * View Form: `project.view_task_form2`
    * tag_ids attribute set to invisible

### Change Log 10/12/2021 | Federico Bau | Task: 10.28 |   13.0.0.1.35-->  13.0.0.1.36

#### UPD /HACK


User of group Project / User can't change fields of project task type. (The one related to the Project) because are
owned by the project. An HACK in order to 'upgrade' the user has been done in method 'write'

* **project.task**
  * Method: `write`

Full explanation

>>>     User of the Project with most minimal entry. THis is because the fields in PROJECT_CATEGORY_FIELDS are 
exposed in the project.task. I tried to add 'groups' to the fields however it seems that it doesnt have affect
because the fields are already created. And manually add the groups into the fields with a scripts seems
overkill (and may cause issue to the DB). 
Right now, the fields are alredy created since a while in production and a delete and re-create them will cause a data loss. 
What was supposed to do since the beginning (if it was known that project.group_project_user needed to change 
the project fields listed in PROJECT_CATEGORY_FIELDS as well) was to create a separeate common table or to add groups='project.group_project_user' in 
this fields (however not sure if this would work neither, hence first solution is the best

### Change Log 1/12/2021 | Federico Bau | Task: 10.30  |   13.0.0.1.34 -->  13.0.0.1.35

### ADD
Add the Type field in the Projects and Tasks tree view
Add tooltip in the Project and Type field in the tree view of projects and tasks
Add the fields in the All tab:
-Fecha Previsión Entrega
- Fecha Final Entrega
- Fecha Inicio 1ª reunión Seguimiento


### Change Log 12/11/2021 | Federico Bau | Task: 10.28  |   13.0.0.1.33 -->  13.0.0.1.34

#### ADD

**Added more project types into the Project tabs and form 
* **project.project,project.task**
  
```text
GENERAL SERVICIOS
-Recepción Documentación/Datos 
-Revisión 
-Entrega Informe 

PROTOCOLO ACOSO SEXUAL /LABORAL
-Entrega protocolo acoso sexual
- Entrega protocolo acoso laboral

GESTION DENUNCIAS ACOSO 
-Activación canal denuncias 

MEDIDAS PREVENCION ACOSO SEXUAL
- Inicio Seguimiento
-Entrega de medidas de prevención 

PLAN NO DISCRIMINACION LGTBI
-Entrega protocolo LGTBI
-Entrega medidas de prevención
```


### Change Log 09/11/2021 | Federico Bau |  13.0.0.1.32-->  13.0.0.1.33

#### UPD

* **project.project, project.task** field `six_n_dpts` from Date to Integer

-----------------------------------------

### Change Log 20/10/2021 | Federico Bau |  13.0.0.1.31 -->  13.0.0.1.32

#### UPD

Merged and Improved functionality from module project_task_timer_app


#### ADD

Added fields in Project which depends on ' project.type.project_type_category' fields selection function,
The selection is mapped with the Project type_id.project_type_category and displays accordingly in the Project
form view ' view_project_task_user_form' 

* **project.project**   
    * Added new fields (see \customize\models\project_project.py under Utility section)
    * new field: project_type_category related - type_id.project_type_category
    * New views: `\customize\views\project_category\project_type_category_views.xml`
* **project.type**
    * New field project_type_category --> Selection
    * New Data: project_type_data.xml wich defines the 6 Categories for GrupoSGP

2 Main features added in the Front-end and JS Framework
1. Tree view header is sticky to the top.
2. Created new Custom Tree View which enables 'Tabs' to the top. These tabs are mapped to the project.project.project_type_category
fields category and will show different list view (defined in `\customize\views\project_category\project_type_category_views.xml`)

* **Fron-End**
    * `customize.ListMultiTab`
        1. Modified the ' ListRenderer' which is the List view, makes the Header of the table sticky 
        2. `AbstractController`, `ControlPanelRenderer` modified
        3. `ListMultiTabController` is a new Custom list view. 


* dependency:
* (Third Party): `project_description, project_category,`



#### REM

* **project.project,project.task*
  * Fields: enable_data,data_sent,data_reception_quali,data_reception_quant,data_forecastdata_delivered,data_sent


### Change Log 20/10/2021 | Federico Bau |  13.0.0.1.30-->  13.0.0.1.31

#### ADD

Removed from project and task view the project_kanban as it has been replace from module`extra_features_gruposgp
project.stage_id  

Change Versions & Extra Features
--------------------------------


### Change Log 20/10/2021 | Federico Bau | 13.0.0.1.29 --> 13.0.0.1.30

#### ADD

* **project.project**
  * Added tracking to fields: `task_user_id_hr, task_user_id_no_limit` (extra_features_gruposgp)
  * Added tracking for `update_task_responsable` method (in customize)
* **project.task**
   * Added tracking to fields: `user_id_hr`  (extra_features_gruposgp)
* **mail.message.subtype**
  * Added 3 new data records: `project_update_task_user_method, project_update_employee_manager, project_update_project_task_user`


### Change Log 11/10/2021 | Federico Bau | 13.0.0.1.28 -> 13.0.0.1.29

* **project.project, project.task**
  * New field: `employee_id_manager m2o -> hr.employee` (Module `extra_features_gruposgp`)
  * Function: `update_task_responsable` (module `customize' ) adds the `employee_id_manager` user_id_no_limit.partner_id to the followers


### Change Log 7/10/2021 | Federico Bau | 13.0.0.1.27 --> 13.0.0.1.28

* **project.task** `user_id_hr` from many2one -> many2many


### Change Log 23rd September - 2021 | Federico Bau | 13.0.0.1.26 --> 13.0.0.1.27

* **project.project**
  * Fields `user_id_hr, task_user_id_hr` became Many2many.
  * fixed function `update_task_responsable`
  * Function `get_main_project_user_hr_id` will determine which is the main Project's user_id


### Change Log 6th September - 2021 | Federico Bau | 13.0.0.1.25 --> 13.0.0.1.26
####TASK 10.13

* **project.task** , **project.project**
    * Added field `data_report_delivered`

### Change Log 2nd September - 2021 | Federico Bau | 13.0.0.1.24 --> 13.0.0.1.25
####TASK 10.13

* **project.task** , **project.project**
    * Added field data_plan_delivered
  
### Change Log 27th July - 2021 | Federico Bau | 13.0.1.0.96 --> 13.0.0.1.23  -> 13.0.0.1.24
####TASK 10.13

* **project.task** 
    * field `kanban_state` is readonly.

### Change Log 22th July - 2021 | Federico Bau | 13.0.1.0.96 --> 13.0.0.1.2  -> 13.0.0.1.23
####TASK 10.13

#REM:     

* **project.project** sale_user_id, sale_agent_id as they are moved to module --> extra_features_gruposgp

1. Delete data_reception (date) 
2.- All these fields (,data_reception_quali, data_reception_quant,data_forecast,data_delivered,enable_meetings,first_meeting,second_meeting,third_meeting,fourth_meeting) must also be modifiable from the tasks
3.- In the tree view of projects and tasks, add the project status field next to the project name
4.- Add the task description field in the tree view of project.task
5.- Project.project & project.task tree view are editable
6. Added sale_user_id, sale_agent_id to project.task Tree View


Change Versions & Extra Features
--------------------------------

### Change Log 30th June - 2021 | Federico Bau | 13.0.1.0.7 --> 13.0.1.0.93
####TASK 10.13

------------------------ < ADD > ------------------------

* depends: extra_features_gruposgp,sale_timesheet
* **project.project** New Fields:
    * enable_data (boolean)  [Enables the below in the Project View]
        * data_sent (date)
        * data_reception (date)
        * data_reception_quali (date)
        * data_reception_quant (date)
        * data_forecast (date)
        * data_delivered (date)
    * enable_meetings (boolean) [Enables the below in the Project View]
        * first_meeting (date)
        * second_meeting (date)
        * third_meeting (date)
        * fourth_meeting (date)
    * sale_user_id: related -> sale_order_id.user_id
    * sale_agent_id: related -> sale_order_id.agent_id

### Change Log 19th June - 2021 | Federico Bau | 13.0.1.0.6 --> 13.0.1.0.7
####TASK 10.6

* **res.partner**
> Added field: message_employee_ids `message_employee_ids` Many2many -> `hr.employee`
> Custom Views: `base.view_res_partner_filter, mail.res_partner_view_activity` in order to use the Activity filter hack

### Change Log 16th June - 2021 | Federico Bau | 13.0.1.0.5--> 13.0.1.0.6
####TASK 10.6

    ---------------------------- < HACK > ----------------------------
    
* Filter for message_employee_ids in sale.order Activity View filters the Sale order as well as the Activities.
HACK:
We Basically controll which Activity Ids we finally deliver to the Front-end. In order for this to work
the following is needed:
For the example we have:
     A) sale.order as Current Model
     B) mail.activity as the Activity model (dah..)
     C) hr.employee filter as Target Field to use to filter Activities
Steps:
      1) A Many2many field to the target DB Model (i.e. hr.employee) within  the **CURRENT MODEL** (i.e sale.order)
      and have the Many2one Field from the mail.activity, these will be used as Hook.

      2) Compute the Field Many2many, just add all Many2one from mail.activity into sale.order

      3) The field must have a reverse search function which search activities based on the name of the hr.employee
      This is used when typing the Name into the search bar (obviousle the filter should be addded in the search view too) 

      4)  With function get_activity_data get the 'domain' parameter and scan the operand. So Add the result to the 
      read_group


    ---------------------------- < ADD > ----------------------------
    
* depends: `base_automation, mass_mailing, sale, project` 

* **base.automation** --> New Field: `employee_id` Many2one -> `hr.employee`
* Added In Views: `base_automation.view_base_automation_search,base_automation.view_base_automation_tree
                  base_automation.view_base_automation_form ` 
* **ir.actions.server**
   * Overwritten function: run_action_next_activity. 
   * **What it does is Adding the  employee_id declared on the Automation rule into the corresponding 
   employee_id of the mail.activity created.
   
* **sale.order** New Field: `message_employee_ids` Many2many -> `hr.employee`

* Qweb: mail.activities-list-group-item Overwritten in order to show the employee_id related to the activity and not the 
user_id:
    * mail.activity_items,mail.activities-list-group-item


   
### Change Log 14th June - 2021 | Federico Bau | 13.0.1.0.4 --> 13.0.1.0.5
####TASK 10.5

    ---------------------------- < ADD > ----------------------------
    
* depends: `mail`

* **mail.activity**
    * Added field: ``employee_id`` Many2one -> `mail.activity`
    * View: `mail_activity_view_tree_custom` Added Create and Import Attrs


###Change Log 11th - June - 2021 (Federico Bau) 13.0.0.0.3 --> 13.0.1.0.4
## TASK 10.4

        -------------- < ADD > --------------

* **project.project**, 
    *  Field: task_user_id_no_limit
    * Function `update_task_responsable`: Now updates the Follower of Project & Task depending on the New fields
* **hr.employee**
    * Field: user_id_no_limit: Many2one to res.user but with no limit. 
    
    

###Change Log 11th - June - 2021 (Federico Bau) 13.0.1.0.0 ---> 13.0.0.0.3
## TASK 10.4


Now changes made affect hr.employee and not res.users
All Views have been updates.

        -------------- < ADD > --------------

* depends: ``hr``
    
* **product.category.agent.commission**
    * Field: ``agent_id_hr``
* **project.project**
    * Field: `task_user_id_hr`, `user_id_hr` (replaces user_id)
    
* **project.task**
    * Field: `user_id_hr` (replaces user_id)
    


#### [ADD]

#### [REM]

#### [FIX]

------------------------------------------


-----------------------------------------------------------------------------------------------------


Requirements
------------

### Oddo's native Modules


### 3rd Party Modules


### Python 3rd Party Packages




-----------------------------------------------------------------------------------------------------


Additional Notes
----------------