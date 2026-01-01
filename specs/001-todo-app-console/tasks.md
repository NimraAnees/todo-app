---
description: "Task list template for feature implementation"
---

# Tasks: Todo App — Phase I: In-Memory Python Console

**Input**: Design documents from `/specs/001-todo-app-console/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python project with directory structure
- [x] T003 [P] Create src/ directory with models/, services/, cli/ subdirectories

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Todo model in src/models/todo.py with id, description, completed, created_at attributes
- [x] T005 Create TodoService in src/services/todo_service.py with all CRUD operations
- [x] T006 Setup in-memory storage structure in TodoService with todos list and next_id tracker
- [x] T007 Create CLI interface in src/cli/cli_interface.py using argparse
- [x] T008 Create main.py entry point that orchestrates CLI and core logic
- [x] T009 Implement error handling and validation for all operations

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with a description via CLI command

**Independent Test**: Can be fully tested by running the add command with a todo description and verifying it appears in the list of todos.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [x] T010 [P] [US1] Unit test for Todo model creation in tests/unit/test_todo.py
- [x] T011 [P] [US1] Unit test for create_todo method in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Todo model with validation rules in src/models/todo.py
- [x] T013 [US1] Implement create_todo method in src/services/todo_service.py
- [x] T014 [US1] Add CLI command handler for 'add' in src/cli/cli_interface.py
- [x] T015 [US1] Connect CLI add command to TodoService create_todo method
- [x] T016 [US1] Add validation for non-empty description (1-500 chars)
- [x] T017 [US1] Add success and error feedback for add operation

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Enable users to see all their current todo items in the console

**Independent Test**: Can be fully tested by adding todos and then running the list command to verify all todos are displayed correctly.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T018 [P] [US2] Unit test for get_all_todos method in tests/unit/test_todo_service.py
- [x] T019 [P] [US2] Integration test for list functionality in tests/integration/test_cli_integration.py

### Implementation for User Story 2

- [x] T020 [P] [US2] Implement get_all_todos method in src/services/todo_service.py
- [x] T021 [US2] Add CLI command handler for 'list' in src/cli/cli_interface.py
- [x] T022 [US2] Connect CLI list command to TodoService get_all_todos method
- [x] T023 [US2] Format output display with ID, description, and status
- [x] T024 [US2] Handle empty list case with appropriate message
- [x] T025 [US2] Add success and error feedback for list operation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Mark Todo Complete/Incomplete (Priority: P2)

**Goal**: Enable users to update the status of a todo item from incomplete to complete or vice versa

**Independent Test**: Can be fully tested by adding a todo, marking it complete, then viewing the list to verify the status has changed.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T026 [P] [US3] Unit test for mark_complete/mark_incomplete methods in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [x] T027 [P] [US3] Implement mark_complete method in src/services/todo_service.py
- [x] T028 [P] [US3] Implement mark_incomplete method in src/services/todo_service.py
- [x] T029 [US3] Add CLI command handler for 'complete' in src/cli/cli_interface.py
- [x] T030 [US3] Add CLI command handler for 'incomplete' in src/cli/cli_interface.py
- [x] T031 [US3] Connect CLI commands to TodoService status update methods
- [x] T032 [US3] Add validation to ensure todo ID exists before updating
- [x] T033 [US3] Add success and error feedback for status update operations

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---
## Phase 6: User Story 4 - Update Todo (Priority: P3)

**Goal**: Enable users to modify the description of an existing todo item

**Independent Test**: Can be fully tested by adding a todo, updating its description, then viewing the list to verify the change.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T034 [P] [US4] Unit test for update_todo method in tests/unit/test_todo_service.py

### Implementation for User Story 4

- [x] T035 [P] [US4] Implement update_todo method in src/services/todo_service.py
- [x] T036 [US4] Add CLI command handler for 'update' in src/cli/cli_interface.py
- [x] T037 [US4] Connect CLI update command to TodoService update_todo method
- [x] T038 [US4] Add validation for non-empty new description (1-500 chars)
- [x] T039 [US4] Add validation to ensure todo ID exists before updating
- [x] T040 [US4] Add success and error feedback for update operation

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---
## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Enable users to remove a todo item from their list

**Independent Test**: Can be fully tested by adding todos, deleting one, then viewing the list to verify only the remaining todos are shown.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T041 [P] [US5] Unit test for delete_todo method in tests/unit/test_todo_service.py

### Implementation for User Story 5

- [x] T042 [P] [US5] Implement delete_todo method in src/services/todo_service.py
- [x] T043 [US5] Add CLI command handler for 'delete' in src/cli/cli_interface.py
- [x] T044 [US5] Connect CLI delete command to TodoService delete_todo method
- [x] T045 [US5] Add validation to ensure todo ID exists before deletion
- [x] T046 [US5] Add success and error feedback for delete operation

**Checkpoint**: All user stories should now be independently functional

---
[Add more user story phases as needed, following the same pattern]

---
## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T047 [P] Documentation updates in README.md
- [x] T048 Code cleanup and refactoring
- [x] T049 Performance optimization for handling 100+ todos
- [x] T050 [P] Additional unit tests in tests/unit/
- [x] T051 Security hardening for input validation
- [x] T052 Run quickstart.md validation

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model creation in tests/unit/test_todo.py"
Task: "Unit test for create_todo method in tests/unit/test_todo_service.py"

# Launch all models for User Story 1 together:
Task: "Create Todo model with validation rules in src/models/todo.py"
```

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence