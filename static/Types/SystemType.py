import static.Types.PanelType as PanelType
import static.Types.StyleType as StyleType
import static.Types.QueryMimic as QueryMimic

class SystemClass:
    def __init__(self, id, name, panels, objects, icon, coloring):
        self.id = id
        self.name = name
        self.panels = panels
        self.objects = objects
        self.icon = icon
        self.coloring = coloring
        self.accent_bar = StyleType.Style.Misc.accent_bar(self.coloring[0], self.coloring[1])

    def get_all_objects(self):
        object_list = []
        for object in self.objects:
            object_list.append(object)
            object_list += object.get_sub_objects()
        return object_list

    def get_head(self):
        title = f"Hello, {self.name}!"
        meta = f'charset="utf-8"'
        link_icon = f'rel="icon" href="static/{self.icon}"'
        link_style = f'rel="stylesheet" href="static/SystemStyles.css"'
        head = f"<meta {meta}/><title> {title} </title><link {link_icon}><link {link_style}>"
        return head

    def get_main_panels(self):
        panels_str = ""
        for panel in self.panels:
            panels_str += f'{panel.__str__()}'
        panels_str = f'<div id=\"SYSTEM_INFO\" class=\"LeftPanel\">{panels_str}</div>'
        return panels_str

    def get_objects(self):
        objects_str = ""
        for object in self.objects:
            objects_str += f'{object.__str__()}'
        objects_str = f'<div class="star-system" onclick="closeSidepanel();closeSystempanel();onHoverLeaveSidepanelButton(\'UNIV_CLOSEBUTTON\',\'{self.coloring[0]}\');onHoverLeaveSidepanelButton(\'STAR_CLOSEBUTTON\',\'{self.coloring[0]}\');"><div id="zeropoint" style="z-index:100;"></div>{objects_str}</div>'
        return objects_str

    def get_accent_bar(self):
        return f'<div {self.accent_bar}></div>'

    def get_panels(self):
        panels_str = ""
        for object in self.objects:
            panels_str += object.get_panels()
        return panels_str

    def get_side_panel_obj(self):
        side_str = ""
        for object in self.get_all_objects():
            side_str += f'<a id="{object.id+"_LABEL"}" {PanelType.Style.Text.sidepanel()} onclick="objClicked(\'{object.id+"_INFO"}\');closeSidepanel();onHoverLeaveSidepanelButton(\'UNIV_CLOSEBUTTON\',\'{self.coloring[0]}\');onHoverLeaveSidepanelButton(\'STAR_CLOSEBUTTON\',\'{self.coloring[0]}\');" onmouseover="onHoverEnter(\'{object.id+"_LABEL"}\',\'{object.color}\');" onmouseout="onHoverLeave(\'{object.id+"_LABEL"}\');">   {object.name}</a>'
        side_str = f'<div id="STAR_SIDEPANEL" class="SidePanel" style="box-shadow: 4px 0 4px {self.coloring[0]};"><a id=\"STAR_CLOSEBUTTON\" {PanelType.Style.Button.close_sidepanel(self.coloring[0])} onclick="closeSidepanel();" onmouseover=\"onHoverEnterSidepanelButton(\'STAR_CLOSEBUTTON\');\" onmouseout=\"onHoverLeaveSidepanelButton(\'STAR_CLOSEBUTTON\',\'{self.coloring[0]}\');\">&#9776; Objects</a><hr>{side_str}</div>'
        return side_str
    
    def get_side_panels(self):
        side_btn_1 = f"<a id=\"STAR_BUTTON\" {PanelType.Style.Button.open_sidepanel()} onclick=\"openSidepanel();\" onmouseover=\"onHoverEnterButton(\'STAR_BUTTON\');\" onmouseout=\"onHoverLeaveButton(\'STAR_BUTTON\');\">&#9776;</a>"
        side_btn_2 = f'<a id=\"UNIV_BUTTON\" {PanelType.Style.Button.open_sidepanel("8vmin")} onclick="openSystempanel();" onmouseover=\"onHoverEnterButton(\'UNIV_BUTTON\');\" onmouseout=\"onHoverLeaveButton(\'UNIV_BUTTON\');\">&#9733;</a>"'
        side_btn_3 = f'<a id=\"BACK_BUTTON\" {PanelType.Style.Button.open_sidepanel("92.5vh")} href="space" onmouseover=\"onHoverEnterButton(\'BACK_BUTTON\');\" onmouseout=\"onHoverLeaveButton(\'BACK_BUTTON\');\">&#8634;</a>'
        return side_btn_1+side_btn_2+side_btn_3

    def get_start_panel(self):
        side_str = f'<a id=\"UNIV_CLOSEBUTTON\" {PanelType.Style.Button.close_sidepanel(self.coloring[0],"8vmin")} onclick="closeSystempanel();" onmouseover=\"onHoverEnterSidepanelButton(\'UNIV_CLOSEBUTTON\');\" onmouseout=\"onHoverLeaveSidepanelButton(\'UNIV_CLOSEBUTTON\',\'{self.coloring[0]}\');\">&#9733; Systems</a><p></p>'
        side_str = f'<div id="UNIVERSE_SIDEPANEL" class="SidePanel" style="box-shadow: 4px 0 4px {self.coloring[0]};">{side_str}{QueryMimic.Mimic.get_falseborne_stars()}</div>'
        return side_str