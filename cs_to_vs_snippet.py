import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_vs_snippet(cs_code, title, description, shortcut):
    """
    將 C# 程式碼轉換成 VS Snippets 格式
    
    Args:
        cs_code (str): C# 程式碼
        title (str): Snippet 標題
        description (str): Snippet 描述
        shortcut (str): 快捷鍵
    """
    # 建立 XML 結構
    root = ET.Element("CodeSnippets")
    root.set("xmlns", "http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet")
    
    snippet = ET.SubElement(root, "CodeSnippet")
    snippet.set("Format", "1.0.0")
    
    # Header 部分
    header = ET.SubElement(snippet, "Header")
    title_elem = ET.SubElement(header, "Title")
    title_elem.text = title
    desc_elem = ET.SubElement(header, "Description")
    desc_elem.text = description
    shortcut_elem = ET.SubElement(header, "Shortcut")
    shortcut_elem.text = shortcut
    
    # Snippet 部分
    snippet_elem = ET.SubElement(snippet, "Snippet")
    code_elem = ET.SubElement(snippet_elem, "Code")
    code_elem.set("Language", "CSharp")
    
    # 處理程式碼中的特殊字元
    cs_code = cs_code.replace("&", "&amp;")
    cs_code = cs_code.replace("<", "&lt;")
    cs_code = cs_code.replace(">", "&gt;")
    cs_code = cs_code.replace('"', "&quot;")
    cs_code = cs_code.replace("'", "&apos;")
    
    code_elem.text = cs_code
    
    # 美化 XML 輸出
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    return xml_str