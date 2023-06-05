/** @odoo-module */

import { registry } from '@web/core/registry';
import { CharField } from '@web/views/fields/char/char_field';
import { formatChar } from '@web/views/fields/formatters';

class TaskTaskNameWithSubtaskCountCharField extends CharField {
    get formattedSubtaskCount() {
        return formatChar(this.props.record.data.child_text || '');
    }
}

TaskTaskNameWithSubtaskCountCharField.template = 'task.TaskTaskNameWithSubtaskCountCharField';

registry.category('fields').add('name_with_subtask_count', TaskTaskNameWithSubtaskCountCharField);