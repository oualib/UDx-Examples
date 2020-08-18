CREATE OR REPLACE LIBRARY printable AS 'printable_idx.py' LANGUAGE 'Python';
CREATE OR REPLACE FUNCTION printable_idx AS LANGUAGE 'Python' NAME 'printable_idx_factory' LIBRARY printable fenced;