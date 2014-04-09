tinymce.create('tinymce.plugins.CodeSyntaxPlugin', {
    createControl: function(n, cm) {
        switch (n) {
            case 'codeformat':
                var mlb = cm.createListBox('codeformat', {
                    title: 'Format Code',
                    onselect: function(v) {
                        var content = String(tinyMCE.activeEditor.selection.getContent());
                        content = content.replace(/<(p)([^>]*)>/g, '');
                        content = content.replace(/<\/(p)>/g, '');
                        //content = content.replace(/\/(&nbsp;)/g, '\n\r');

                        tinyMCE.activeEditor.selection.setContent('<pre id=\'code\' name=code class="' + v + '">' + content + '</pre>');
                    }
                });

                // Add some values to the list box
                mlb.add('Python', 'python');
                mlb.add('JavaScript', 'javascript');

                // Return the new listbox instance
                return mlb;
        }

        return null;
    },

    getInfo: function() {
        return {
            longname: 'Code Syntax Plugin',
            author: 'Jacobus Meintjes',
            authorurl: 'http://www.phoenixcode.net',
            infourl: 'http://alexgorbatchev.com/wiki/SyntaxHighlighter',
            version: '1.0'
        };
    }
});

    // Register plugin with a short name
    tinymce.PluginManager.add('codesyntax', tinymce.plugins.CodeSyntaxPlugin);