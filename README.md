# convert_bibliogrph_links_to_templates_and_remove_yandex.slovari
Wiki: Полуавтоматический конвертор библиографических ссылок на книги/статьи в определённые библиографические шаблоны. Работает по определённому url. На момент заливки на github настроен на замену библиографических ссылок на умерший сервис Yandex.Slovari.ru, удаляя их. 

Обрабатывает 1 данную страницу, запускается из другого бота (например, из AWB файлом .vbs) для страниц подставляемых ботом по списку.

Использует:
* парсер вики-разметки: https://github.com/earwig/mwparserfromhell  
* Мою библиотеку под этот парсер lib_for_mwparserfromhell: https://github.com/vladiscripts/commons_libs

