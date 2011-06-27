function CustomFileBrowser(field_name, url, type, win) {
    
    var cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;
    
    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 640,  // Your dimensions may differ - toy around with them!
        height: 480,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no',
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId,
    });
    return false;
}

tinyMCE.init({
	mode : "textareas",
	theme : "advanced",
	file_browser_callback : "CustomFileBrowser",
	
	// Layout
	width: 758,
	height: 400,
	indentation: '10px',
		
	//content_css : "/appmedia/blog/style.css",
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_buttons1 : "formatselect, styleselect, separator, fullscreen,separator,preview,separator,bold,italic,underline,strikethrough,separator,bullist,numlist,outdent,indent,separator,undo,redo,separator,justifyleft,justifycenter,justifyright,separator,link,unlink,anchor,separator,image,media,cleanup,help,separator,code",
	theme_advanced_buttons2 : "",
	theme_advanced_buttons3 : "",
	
	theme_advanced_blockformats: 'p,h2,h3,h4,pre',	
	
	// Style formats
	// see http://wiki.moxiecode.com/index.php/TinyMCE:Configuration/style_formats
	style_formats : [
		{title : 'Paragraph Small', block : 'p', classes: 'p_small'},
		{title : 'Paragraph ImageCaption', block : 'p', classes: 'p_caption'},
		{title : 'Clearfix', block : 'p', classes: 'clearfix'},
		{title : 'Code', block : 'p', classes: 'code'}
	],
	
	// Adv
	advlink_styles: 'Internal Link=internal;External Link=external',
	advimage_update_dimensions_onchange: true,
    
	// Grappelli
	grappelli_adv_hidden: false,
	grappelli_show_documentstructure: 'on',	
	
	auto_cleanup_word : true,
	plugins : "table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,searchreplace,print,contextmenu,fullscreen",
	plugin_insertdate_dateFormat : "%m/%d/%Y",
	plugin_insertdate_timeFormat : "%H:%M:%S",
	extended_valid_elements : "a[name|href|target=_blank|title|onclick],img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
	fullscreen_settings : {
		theme_advanced_path_location : "top",
		theme_advanced_buttons1 : "fullscreen,separator,preview,separator,media,cut,copy,paste,separator,undo,redo,separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,help",
		theme_advanced_buttons2 : "removeformat,styleselect,formatselect,fontselect,fontsizeselect,separator,bullist,numlist,outdent,indent,separator,link,unlink,anchor",
		theme_advanced_buttons3 : "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,advhr,visualaid,separator,charmap,emotions,iespell,flash,separator,print"
	}
});
