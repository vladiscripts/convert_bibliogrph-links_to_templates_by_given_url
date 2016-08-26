# -*- coding: utf-8  -*-
#
# author: https://github.com/vladiscripts
#
import sys
import mwparserfromhell
from lib_for_mwparserfromhell import *

filename = r'../temp/AWBfile.txt'  # страница в вики-разметке
text = file_readtext(filename)

# text = r'''* {{Из|БСЭ|http://slovari.yandex.ru/Дербент/БСЭ/Дербент/|заглавие=Дербент}}
# '''

ParametersToRemove = (
	'место', 'издательство', 'язык', 'тип', 'год', 'ответственные', 'publisher', 'archiveurl', 'archivedate',
	'accessdate')

dics = [
	{
		'renameTemplateTo': 'Книга:Городские имена сегодня и вчера|1997|заглавие=',
		'urlPartWithPagename': r'Петербургская%20топонимика|%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D1%81%D0%BA%D0%B0%D1%8F%20%D1%82%D0%BE%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B8%D0%BA%D0%B0',
		'addSignature': r'|dict/petertoponim',
		'paramTitle': 'заглавие',
		'paramAuthor': '',
	},
	{
		'renameTemplateTo': 'Книга:Энциклопедия «Москва» 1997',
		'urlPartWithPagename': r'Энциклопедия%20«Москва»|%D0%AD%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F%20%C2%AB%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%C2%BB|Энциклопедия%20%C2%ABМосква%C2%BB',
		'addSignature': r'|dict/mos',
		'paramTitle': '1',
		'paramAuthor': 'автор',
	},
	{
		'renameTemplateTo': 'Имена московских улиц',
		'urlPartWithPagename': r'Московские%20улицы|%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5%20%D1%83%D0%BB%D0%B8%D1%86%D1%8B',
		'addSignature': r'|dict/mostoponim',
		'paramTitle': '1',
		'paramAuthor': 'автор',
	},
	{
		'renameTemplateTo': 'Из БОЭ',
		'urlPartWithPagename': r'Олимпийская%20энциклопедия|%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F%20%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F',
		'addSignature': r'|dict/olympic',
		'paramTitle': 'title',
		'paramAuthor': 'автор',
	},
	{
		'renameTemplateTo': 'Революционеры',
		'urlPartWithPagename': r'Революционеры|%D0%A0%D0%B5%D0%B2%D0%BE%D0%BB%D1%8E%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%8B',
		'addSignature': r'|dict/revoluc',
		'paramTitle': '1',
		'paramAuthor': 'автор',
	},
	{
		'renameTemplateTo': r'Отечественные певцы 1750-1917',
		'urlPartWithPagename': r'Отечественные%20певцы|%D0%9E%D1%82%D0%B5%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%B5%D0%B2%D1%86%D1%8B',
		'addSignature': '',
		'paramTitle': '1',
		'paramAuthor': 'автор',
	},
	# {
		# renameTemplateTo : 'Кто есть кто в современной культуре‎‎',
		# 'addSignature': 'dict/who-is-who',
		# pagenameFromLink : r'/(?:Кто%20есть%20кто%20в%20культуре/|%D0%9A%D1%82%D0%BE%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%BA%D1%82%D0%BE%20%D0%B2%20%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B5/)([^]|/?&}\n]+)/?',
		# link2removebase : r'Кто%20есть%20кто%20в%20культуре|%D0%9A%D1%82%D0%BE%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%BA%D1%82%D0%BE%20%D0%B2%20%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B5|dict/who-is-who',
	# },
	{
		'renameTemplateTo': r'Вокально-энциклопедический словарь',
		'urlPartWithPagename': r'Вокально-энциклопедический%20словарь|%D0%92%D0%BE%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C',
		'addSignature': r'|dict/agin',
		'paramTitle': '1',
		'paramAuthor': 'автор',
	},
	# {
		# renameTemplateToIzBSE : 'Из БСЭ'
		# pagenameFromLink : r'/(?:БСЭ/|%D0%91%D0%A1%D0%AD/|article.xml\?book=bse&title=|dict/bse)(?:/[^]/}]*)?/([^]|/?&}\s\n]+)'
		# pagenameFromLink : r'/(?:БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)(?:/[^]/}]*)?/(?:\d+/\d+\.htm\?text=)?([^]/}\s\n]+)'
		# pagenameFromLink : r'/(?:БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)(?:/[^]/}]*)?/([^]|/?&}\s\n]+)'  (?:/[^]/}]*)?
	# },
	]
link2removeSY = r'https?://(?:www\.|m\.)?slovari\.yandex\.ru'

code = mwparserfromhell.parse(text)

reSymbols = r'[.,;:›"/\s—−-]*'
reEnd = reSymbols + '$'
reBegin = '^' + reSymbols
reTire = r'[\s—−-]+'
reV = r'(?:\b(?:в|из|на)\s+)?'
reBSE = reSymbols + r'\(?["«]*(?:\[\[)?(?:БСЭ|[Бб]ольш(ая|ой) [Сс]оветск(ая|ой) [Ээ]нциклопеди[яи])(?:\]\])?["»]*\)?[.,:;\s›—−-]*'
reYS = r'["\'«]?(Яндекс[е]?[.\s]*(?:Словар(?:[еьи]|ях))?|(?:slovari.)?yandex.ru)["\'»]?'
reRemoveFromTitles = [
	# r'.*',  # внимание: это удаление всего заголовка ссылки, для взятия его из url. только для словарей с именем в url
	r'(в )?[Сс]ловар(?:[еьи]|ях)?.*?(?:на )?(?:сайте )?' + reYS,
	r'(?:Биография|Данные)? (?:на )?(?:сайте )?' + reYS,
	# r'["\'«]?(?:[Яя]ндекс|[Yy]andex)[.\s:-]*(?:[Сс]ловари|[Ss]lovari)["\'»]?',
	r'[Сс]ловари',
	'Биография',
	r'{{мёртвая ссылка\|число=14\|месяц=06\|год=2016}}',
	r'(?:\[\[Пружанский, Аркадий Михайлович\|)?Пружанский\s*А.\s*М.(?:&#93;&#93;)?\s*Отечественные певцы. 1750[\s—−-]+1917: Словарь.[\s—−-]+Изд. 2-е испр. и доп., электронное.[\s—−-]+М., 2008',
	# r'(?:В 30 т.)?[—−/ -]*М.: "?Советская энциклопедия"?[,.] 1969[—−/ -]*1978',
	# r'(?:в (?:словаре|энциклопедиии|книге|справочнике) )?["«]*Кто есть кто в(?: современной)? культуре["»]*',
	r'(?:в\s+(?:словаре|энциклопедии|книге|справочнике)\s*)?["«]*Отечественные певцы["»]*',
	r'[\s.]*Эксклюзивные биографии.[\s—−-]+Выпуск 1[\s—−-]+2.[\s—−-]+М.: МК[\s—−-]+Периодика, 2006[\s—−-]+2007\.?',
	r'[[\s]*(Агин, Михаил Суренович\|)?Агин М\.\s*С\.[]\s]*(?:&#93;{{мёртвая ссылка\|число=14\|месяц=06\|год=2016}}&#93;)?\s*Вокально-энциклопедический словарь. \(?Биобиблиография\)?. В 5 т.[\s—−-]+М.,\s*1991[\s—−-]+1994\]*',
	r'Вокально-энциклопедический словарь(?:, 1991-1994)?',
	r'Отечественные певцы(?:[.\s—−-]+2008)?',	
	r'(?:Энциклопедия|в [Ээ]нциклопедии) ["«]*Москва["»]*',
	r'М.: БРЭ, 1997',
	r'Петербургская топонимика',
	# r'На Яндекс[.:\s]*[Тт]опонимика',
	'<!-- Заголовок добавлен ботом -->',
	r'^Биография' + reV + reBSE,
	r'^Биография$',
	r'Электронная версия',
	reSymbols + reV + reYS,
	r'1969[\s—−-]*1978',
	r'\d-е изд(?:\.|ание)?',
	reSymbols + reV + reBSE,
	r'[Сс]татья' + reV,
	reBegin,
	reEnd,
	]

for dic in dics:
	pagenameFromLink = r'/(?:' + dic['urlPartWithPagename'] + r')/([^]|/?&}\n]+)/?'
	link2remove_DicSignature = dic['urlPartWithPagename'] + dic['addSignature']
	link2remove = link2removeSY + r'/[^|\s]*(' + str(link2remove_DicSignature) + ')'

	for template in code.filter_templates():
		if template.name.matches(('cite web', 'cite news')) and findLink(template, link2remove):
			newtpl = mwparserfromhell.nodes.template.Template(dic['renameTemplateTo'])
			if template.has('title'):
				title = str(template.get('title').value.strip())
				newtpl.add(dic['paramTitle'], title)
			if template.has('author') and template.get('author').value != '':
				title = str(template.get('author').value.strip())
				newtpl.add(dic['paramAuthor'], title)	
			code.replace(template, str(newtpl))			
			
	for template in code.filter_templates():
		if template.name.matches(('книга')) and findLink(template, link2remove):
			newtpl = mwparserfromhell.nodes.template.Template(dic['renameTemplateTo'])
			if template.has('заглавие'):
				title = str(template.get('заглавие').value.strip())
				newtpl.add(dic['paramTitle'], title)
			if template.has('автор') and template.get('автор').value != '':
				title = str(template.get('автор').value.strip())
				newtpl.add(dic['paramAuthor'], title)	
			code.replace(template, str(newtpl))		

	link2template(code, link2remove, dic['renameTemplateTo'], 'ссылка', dic['paramTitle'], reRemoveFromTitles, pagenameFromLink)
				

text = str(code)
file_savetext(filename, text)
