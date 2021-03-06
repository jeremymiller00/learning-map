# learning-map
My path to continual data science improvement.

An cli application for viewing and interacting with my Data Scientist Learning Map. The Learning Map represents books, tutorials, courses to develop my data science competencies. The application uses Python, Typer, Sqlite3, Pytest, and Loguru.

## Competencies:
1. Machine Learning
2. Software Engineering Skills, primarily to support development and deployment of models
3. Product Management Skills
4. Company product, market, user awareness

## Application User Story
As a data scientist who wants to continually be developing my skills is ways that will make me more productive and effective, I want to be able to store learning items for future action, track progress of learning items, and store what items have been to completed. I want to record and understand what progress I am making towards my defined competencies and where I may need to adjust my plan.

## Application Requirements
The application should have 2-4 clearly defined competencies, which may be updated regularly but should not be changed often. Any more than 2-3 changes per year is sign that they were likely poorly specified.

The application should have a datastore in which individual learning items are persisted. Each item should have a name, be linked to a competency, have start and stop dates, contain a link to the material (is such a link exists), and allow space to record notes.

There should be a kanban-like interface that allows the  user to quickly see which items are in the backlog, which are in process, and  which have been completed, as well as the relative priority of each item. The user should be able to quickly move items from one category to another, and understand which competency each item supports.

There should be a timeline view were the user can view progress over time. It should be easy to understand both the volume if items in process and completed, as well as the relative balance across competencies.

The basic CRUD operations must be supported as follows:
* Create new item. Item attributes are:
  * Name - required
  * Competency - required
  * Type - required
  * Date Started - not required
  * Date Finished - not required
  * Status - required
  * Notes - not required
  * Links - not required

* Read the set of items. Items should be grouped by status: TODO -> INPROGRESS -> DONE
  * There should be a kanban-like view with each item on a "card"
  * There should also be a timeline view such as a gantt chart
  * A secondary requirement is to be able to perform basic analytics over the learning items

* Update items by moving them from one status to another

* Delete items which are not yet completed and are no longer relevant. Any item completed should never be deleted. 

## Success Criteria
* A working application in github which can be cloned to any machine and used. The data are persisted to the cloud. 
