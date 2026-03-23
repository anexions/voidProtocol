import re
import json

path = r"C:\Users\Jesus\Desktop\voidProject\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update CSS flags
css_new = """        .flag-btn.es { border-color: #ffcc00; box-shadow: 0 0 15px rgba(255, 0, 0, 0.4); }
        .flag-btn.en { border-color: #0044ff; box-shadow: 0 0 15px rgba(0, 68, 255, 0.4); }
        .flag-btn.fr { border-color: #fff; box-shadow: 0 0 15px rgba(0, 85, 164, 0.4); }
        .flag-btn.ru { border-color: #d52b1e; box-shadow: 0 0 15px rgba(0, 57, 166, 0.4); }
        .flag-btn.pt { border-color: #009c3b; box-shadow: 0 0 15px rgba(255, 223, 0, 0.4); }"""
text = re.sub(r'        \.flag-btn\.es \{.*?\n        \.flag-btn\.en \{.*?\n', css_new + '\n', text)

# 2. Update HTML flags
html_flags = """                <div class="lang-flags" style="margin-top: 15px;">
                    <button class="flag-btn es active" onclick="setLanguage('es')">[ ES ]</button>
                    <button class="flag-btn en" onclick="setLanguage('en')">[ EN ]</button>
                    <button class="flag-btn fr" onclick="setLanguage('fr')">[ FR ]</button>
                    <button class="flag-btn ru" onclick="setLanguage('ru')">[ RU ]</button>
                    <button class="flag-btn pt" onclick="setLanguage('pt')">[ PT ]</button>
                </div>"""
text = re.sub(r'                <div class="lang-flags"[^>]*>\n                    <button class="flag-btn es active" onclick="setLanguage\(\'es\'\)">\[ ES \]</button>\n                    <button class="flag-btn en" onclick="setLanguage\(\'en\'\)">\[ EN \]</button>\n                </div>', html_flags, text)

html_flags_mob = """        <div class="lang-flags" style="margin-bottom: 30px; position: absolute; top: 40px;">
            <button class="flag-btn es active" onclick="setLanguage('es')">[ ES ]</button>
            <button class="flag-btn en" onclick="setLanguage('en')">[ EN ]</button>
            <button class="flag-btn fr" onclick="setLanguage('fr')">[ FR ]</button>
            <button class="flag-btn ru" onclick="setLanguage('ru')">[ RU ]</button>
            <button class="flag-btn pt" onclick="setLanguage('pt')">[ PT ]</button>
        </div>"""
text = re.sub(r'        <div class="lang-flags"[^>]*>\n            <button class="flag-btn es active" onclick="setLanguage\(\'es\'\)">\[ ES \]</button>\n            <button class="flag-btn en" onclick="setLanguage\(\'en\'\)">\[ EN \]</button>\n        </div>', html_flags_mob, text)

# 3. Add to i18n
lang_json = """        fr: {
            title_main: 'VOID PROTOCOL <span style="font-size: 1.1rem; opacity: 0.7; vertical-align: middle; letter-spacing: 2px;">v1.0</span>',
            btn_achievements: '🏆 SUCCÈS', btn_instructions: '📋 INSTRUCTIONS', btn_ranking: '👑 CLASSEMENT', ach_modal_title: 'REGISTRE DES TITRES', ach_unlocked: 'SUCCÈS DÉVERROUILLÉ!', ach_reward_lbl: 'TITRE:',
            support_txt: 'SOUTENIR LE PROJET:', donate_kofi: '☕ KO-FI', donate_paypal: '💳 PAYPAL', visit_counter: 'VOUS ÊTES LE VOYAGEUR:',
            ui_resources: 'RESSOURCES:', ui_energy: 'ÉNERGIE:', ui_kills: 'Élimin.:', ui_time: 'Temps:', ui_waves: 'VAGUES:',
            tut_defenses_title: 'DÉFENSES', tut_orb_click: 'CLIC:', tut_orb_desc: 'Orbe d\\'énergie. Attaque rapide.',
            tut_grav_click: 'CTRL+CLIC:', tut_grav_desc: 'Graviton. Ralentit et attire.',
            tut_mega: 'MÉGA-TIR:', tut_mega_desc: 'Auto /15 kills. Tir total.',
            tut_threats_title: 'MENACES', tut_nemesis: 'NEMESIS:', tut_nemesis_desc: 'Essaim basique.',
            tut_elite: 'ÉLITE:', tut_elite_desc: 'Grands et tenaces.', tut_frag: 'FRAGMENT:', tut_frag_desc: 'Se divise en 2 à mort.',
            tut_powers_title: 'POUVOIRS', tut_haste: 'SURCHARGE:', tut_haste_desc: 'Cadence de tir max.',
            tut_heal: 'RÉPARER:', tut_heal_desc: 'Restaura l\\'énergie du Noyau.', tut_pause: 'PAUSE:', tut_pause_desc: 'Options audio.',
            tut_clean: 'INTERFACE:', tut_clean_desc: 'Affiche/Masque l\\'interface.', tut_start: 'LANCER LA MISSION',
            pause_title: 'PAUSE', pause_resume: 'REPRENDRE', pause_restart: 'RECOMMENCER', pause_menu: 'MENU PRINCIPAL',
            tut_briefing: 'MISSION BRIEFING // INITIALISATION...',
            tut_mana_info: '⚠️ PROTOCOLE Rc: TOUTE ACTION CONSOMME DES RESSOURCES. ÉLIMINEZ DES ENNEMIS.',
            cost_15: 'Coût: 15 Rc', cost_60: 'Coût: 60 Rc', cost_free: 'Coût: 0 Rc',
            mobile_title: 'VOID PROTOCOL', mobile_msg: '⚠️ ACCÈS REFUSÉ ⚠️', mobile_sub: 'NÉCESSITE UN PC.',
            mega_kills: 'Kills', ranking_title: 'CLASSEMENT MONDIAL', ranking_conn: 'CONNEXION...',
            ranking_col_name: 'NOM - TITRE', ranking_col_wave: 'VAGUE', ranking_col_kills: 'KILLS',
            gameover_title: 'NOYAU DÉTRUIT', gameover_history: 'Historique Récent:', gameover_retry: 'Nouvelle Partie',
            pause_phrases: ["Prenez votre temps...", "Respirez profondément.", "Le Noyau vous attendra.", "Les commandants ont besoin de pauses."],
            audio_on: '🔊 AUDIO: ON', audio_off: '🔇 AUDIO: OFF', ui_visible: 'UI: VISIBLE', ui_hidden: 'UI: MASQUÉ',
            shake_on: '📹 SECOUSSE: ON', shake_off: '📹 SECOUSSE: OFF',
            plus_energy: '+1 ÉNERGIE', nemesis_warning: '⚠️ NÉMÉSIS DIVINE DÉTECTÉE ⚠️', combo: 'COMBO',
            stats_kills: 'Élimin.:', stats_wave: 'Vague:', stats_survived: 'Survécu:',
            history_record: 'RECORD:', history_waves: 'Vagues', history_empty: 'Aucun record précédent.',
            perks: ["", "DÉGÂTS & MANA x2", "TIR RAPIDE", "GRAVITÉ LÉTALE", "NOYAU EXPLOSIF", "PORTÉE SUPRÊME", "SURCHARGE CRITIQUE", "RÉPARATION AUTO", "ANNIHILATION TOTALE"]
        },
        ru: {
            title_main: 'VOID PROTOCOL <span style="font-size: 1.1rem; opacity: 0.7; vertical-align: middle; letter-spacing: 2px;">v1.0</span>',
            btn_achievements: '🏆 ДОСТИЖЕНИЯ', btn_instructions: '📋 ИНСТРУКЦИИ', btn_ranking: '👑 РЕЙТИНГ', ach_modal_title: 'РЕЕСТР ТИТУЛОВ', ach_unlocked: 'ДОСТИЖЕНИЕ РАЗБЛОКИРОВАНО!', ach_reward_lbl: 'ТИТУЛ:',
            support_txt: 'ПОДДЕРЖАТЬ ПРОЕКТ:', donate_kofi: '☕ KO-FI', donate_paypal: '💳 PAYPAL', visit_counter: 'ВЫ ПУТЕШЕСТВЕННИК НОМЕР:',
            ui_resources: 'РЕСУРСЫ:', ui_energy: 'ЭНЕРГИЯ:', ui_kills: 'Убийства:', ui_time: 'Время:', ui_waves: 'ВОЛНЫ:',
            tut_defenses_title: 'ЗАЩИТА', tut_orb_click: 'КЛИК:', tut_orb_desc: 'Сфера энергии. Быстрая атака.',
            tut_grav_click: 'CTRL+КЛИК:', tut_grav_desc: 'Гравитон. Замедляет.',
            tut_mega: 'МЕГА-ВЫСТРЕЛ:', tut_mega_desc: 'Авто за 15 убийств.',
            tut_threats_title: 'УГРОЗЫ', tut_nemesis: 'НЕМЕЗИДА:', tut_nemesis_desc: 'Базовый рой.',
            tut_elite: 'ЭЛИТА:', tut_elite_desc: 'Крупные и прочные.', tut_frag: 'ОСКОЛОК:', tut_frag_desc: 'Делится на 2.',
            tut_powers_title: 'СПОСОБНОСТИ', tut_haste: 'ПЕРЕГРУЗКА:', tut_haste_desc: 'Макс. скорость.',
            tut_heal: 'РЕМОНТ:', tut_heal_desc: 'Восстанавливает энергию.', tut_pause: 'ПАУЗА:', tut_pause_desc: 'Аудио и настройки.',
            tut_clean: 'ИНТЕРФЕЙС:', tut_clean_desc: 'Скрыть/Показать интерфейс.', tut_start: 'НАЧАТЬ МИССИЮ',
            pause_title: 'ПАУЗА', pause_resume: 'ПРОДОЛЖИТЬ', pause_restart: 'ПЕРЕЗАГРУЗИТЬ', pause_menu: 'МЕНЮ',
            tut_briefing: 'МИССИЯ // ИНИЦИАЛИЗАЦИЯ...',
            tut_mana_info: '⚠️ ПРОТОКОЛ Rc: ДЕЙСТВИЯ РАСХОДУЮТ РЕСУРСЫ. УНИЧТОЖАЙТЕ ВРАГОВ.',
            cost_15: 'Цена: 15 Rc', cost_60: 'Цена: 60 Rc', cost_free: 'Цена: 0 Rc',
            mobile_title: 'VOID PROTOCOL', mobile_msg: '⚠️ ДОСТУП ЗАПРЕЩЕН ⚠️', mobile_sub: 'СИСТЕМА ТРЕБУЕТ ПК.',
            mega_kills: 'Убийств', ranking_title: 'МИРОВОЙ РЕЙТИНГ', ranking_conn: 'ПОДКЛЮЧЕНИЕ...',
            ranking_col_name: 'ИМЯ - ТИТУЛ', ranking_col_wave: 'ВОЛНА', ranking_col_kills: 'УБИЙСТВА',
            gameover_title: 'ЯДРО РАЗРУШЕНО', gameover_history: 'История:', gameover_retry: 'Новая игра',
            pause_phrases: ["Сделайте глубокий вдох.", "Отличная тактика - выпить воды.", "Ядро подождет.", "Всем нужен перерыв."],
            audio_on: '🔊 АУДИО: ВКЛ', audio_off: '🔇 АУДИО: ВЫКЛ', ui_visible: 'UI: ВИДИМЫЙ', ui_hidden: 'UI: СКРЫТЫЙ',
            shake_on: '📹 ТРЯСКА: ВКЛ', shake_off: '📹 ТРЯСКА: ВЫКЛ',
            plus_energy: '+1 ЭНЕРГИЯ', nemesis_warning: '⚠️ БОЖЕСТВЕННАЯ НЕМЕЗИДА ⚠️', combo: 'КОМБО',
            stats_kills: 'Убийства:', stats_wave: 'Волна:', stats_survived: 'Выживание:',
            history_record: 'РЕКОРД:', history_waves: 'Волны', history_empty: 'Нет рекордов.',
            perks: ["", "УРОН И МАНА x2", "БЫСТРЫЙ ОГОНЬ", "СМЕРТЕЛЬНАЯ ГРАВИТАЦИЯ", "ВЗРЫВНОЕ ЯДРО", "ВЫСШИЙ РАДИУС", "КРИТ. ПЕРЕГРУЗКА", "АВТОРЕМОНТ", "ПОЛНОЕ УНИЧТОЖЕНИЕ"]
        },
        pt: {
            title_main: 'VOID PROTOCOL <span style="font-size: 1.1rem; opacity: 0.7; vertical-align: middle; letter-spacing: 2px;">v1.0</span>',
            btn_achievements: '🏆 CONQUISTAS', btn_instructions: '📋 INSTRUÇÕES', btn_ranking: '👑 RANKING', ach_modal_title: 'REGISTRO DE TÍTULOS', ach_unlocked: 'CONQUISTA DESBLOQUEADA!', ach_reward_lbl: 'TÍTULO:',
            support_txt: 'APOIE O PROJETO:', donate_kofi: '☕ KO-FI', donate_paypal: '💳 PAYPAL', visit_counter: 'VOCÊ É O VIAJANTE NÚMERO:',
            ui_resources: 'RECURSOS:', ui_energy: 'ENERGIA:', ui_kills: 'Abates:', ui_time: 'Tempo:', ui_waves: 'ONDAS:',
            tut_defenses_title: 'DEFESAS', tut_orb_click: 'CLIQUE:', tut_orb_desc: 'Orbe de energia. Ataque letal.',
            tut_grav_click: 'CTRL+CLIQUE:', tut_grav_desc: 'Graviton. Atrasa e puxa.',
            tut_mega: 'MEGA-TIRO:', tut_mega_desc: 'Auto a cada 15 abates.',
            tut_threats_title: 'AMEAÇAS', tut_nemesis: 'NEMESIS:', tut_nemesis_desc: 'Enxame básico.',
            tut_elite: 'ELITE:', tut_elite_desc: 'Maiores e difíceis.', tut_frag: 'FRAGMENTO:', tut_frag_desc: 'Divide-se em 2 ao morrer.',
            tut_powers_title: 'PODERES', tut_haste: 'SOBRECARGA:', tut_haste_desc: 'Cadência máxima de tiro.',
            tut_heal: 'REPARAR:', tut_heal_desc: 'Restaura energia do Núcleo.', tut_pause: 'PAUSA:', tut_pause_desc: 'Pausa e opções.',
            tut_clean: 'INTERFACE:', tut_clean_desc: 'Oculta/Mostra painéis.', tut_start: 'INICIAR MISSÃO',
            pause_title: 'PAUSA', pause_resume: 'RETOMAR', pause_restart: 'REINICIAR', pause_menu: 'MENU',
            tut_briefing: 'MISSÃO // INICIALIZANDO...',
            tut_mana_info: '⚠️ PROTOCOLO Rc: TODA AÇÃO CONSOME RECURSOS. ELIMINE INIMIGOS PARA REABASTECER.',
            cost_15: 'Custo: 15 Rc', cost_60: 'Custo: 60 Rc', cost_free: 'Custo: 0 Rc',
            mobile_title: 'VOID PROTOCOL', mobile_msg: '⚠️ ACESSO NEGADO ⚠️', mobile_sub: 'ESTE SISTEMA REQUER UM PC.',
            mega_kills: 'Abates', ranking_title: 'RANKING GLOBAL', ranking_conn: 'CONECTANDO...',
            ranking_col_name: 'NOME - TÍTULO', ranking_col_wave: 'ONDA', ranking_col_kills: 'ABATES',
            gameover_title: 'NÚCLEO DESTRUÍDO', gameover_history: 'Histórico Recente:', gameover_retry: 'Jogar Novamente',
            pause_phrases: ["Beba uma água, ótima tática.", "O Núcleo vai esperar por você.", "Calculando próximos movimentos.", "Respire fundo."],
            audio_on: '🔊 ÁUDIO: ON', audio_off: '🔇 ÁUDIO: OFF', ui_visible: 'UI: VISÍVEL', ui_hidden: 'UI: OCULTA',
            shake_on: '📹 TREMOR: ON', shake_off: '📹 TREMOR: OFF',
            plus_energy: '+1 ENERGIA', nemesis_warning: '⚠️ NÊMESIS DIVINA DETECTADA ⚠️', combo: 'COMBO',
            stats_kills: 'Abates:', stats_wave: 'Onda:', stats_survived: 'Sobreviveu:',
            history_record: 'RECORDE:', history_waves: 'Ondas', history_empty: 'Sem registros.',
            perks: ["", "DANO E MANA x2", "TIRO RÁPIDO", "GRAVIDADE LETAL", "NÚCLEO EXPLOSIVO", "ALCANCE SUPREMO", "SOBRECARGA CRÍTICA", "REPARO AUTO", "ANIQUILAÇÃO TOTAL"]
        },
        en: {"""
text = text.replace('        en: {', lang_json)

# 4. Process Achievements via code
def replace_ach(match):
    line = match.group(0)
    if "first_blood" in line: return line.replace("check:", "fr: 'Premier Sang', d_fr: 'Éliminez votre premier drone ennemi.', r_fr: 'Équipier', ru: 'Первая Кровь', d_ru: 'Уничтожьте первый вражеский дрон.', r_ru: 'Экипаж', pt: 'Primeiro Contato', d_pt: 'Elimine seu primeiro drone inimigo.', r_pt: 'Tripulante', check:")
    if "graviton_master" in line: return line.replace("check:", "fr: 'Champ de Singularité', d_fr: 'Construisez votre premier Graviton.', r_fr: 'Tacticien', ru: 'Сингулярность', d_ru: 'Постройте первый Гравитон.', r_ru: 'Тактик', pt: 'Campo de Singularidade', d_pt: 'Construa seu primeiro Graviton tático.', r_pt: 'Tático', check:")
    if "wave_5" in line: return line.replace("check:", "fr: 'Défenseur Novice', d_fr: 'Résistez jusqu\\'à la Vague 5.', r_fr: 'Garde', ru: 'Новичок Защитник', d_ru: 'Доживите до 5-й Волны.', r_ru: 'Страж', pt: 'Defensor Novato', d_pt: 'Resista à tempestade até a Onda 5.', r_pt: 'Guarda', check:")
    if "planet_1" in line: return line.replace("check:", "fr: 'Puissance Incrémentale', d_fr: 'Débloquez l\\'amélioration max.', r_fr: 'Soldat', ru: 'Инкрементальная Сила', d_ru: 'Разблокируйте улушение.', r_ru: 'Солдат', pt: 'Poder Incremental', d_pt: 'Desbloqueie a melhoria de Nível 1.', r_pt: 'Soldado', check:")
    if "first_haste" in line: return line.replace("check:", "fr: 'Surcharge Absolue', d_fr: 'Déclenchez la Surcharge [1].', r_fr: 'Berserker', ru: 'Абсолютная Перегрузка', d_ru: 'Используйте Перегрузку [1].', r_ru: 'Берсерк', pt: 'Sobrecarga Absoluta', d_pt: 'Ative a Sobrecarga [1] pela primeira vez.', r_pt: 'Berserker', check:")
    if "first_heal" in line: return line.replace("check:", "fr: 'Maintenance Critique', d_fr: 'Exécutez une Réparation d\\'urgence.', r_fr: 'Ingénieur', ru: 'Критическое Обслуживание', d_ru: 'Используйте Экстренный Ремонт.', r_ru: 'Инженер', pt: 'Manutenção Crítica', d_pt: 'Execute um Reparo de emergência.', r_pt: 'Engenheiro', check:")
    if "combo_10" in line: return line.replace("check:", "fr: 'Maître des Combos', d_fr: 'Atteignez un Combo x10.', r_fr: 'Spécialiste', ru: 'Мастер Комбо', d_ru: 'Достигните Комбо x10.', r_ru: 'Специалист', pt: 'Mestre do Combo', d_pt: 'Alcance um Combo x10 seguido.', r_pt: 'Especialista', check:")
    if "neon_treasury" in line: return line.replace("check:", "fr: 'Trésor Néon', d_fr: 'Conservez 500 Rc simultanément.', r_fr: 'Banquier', ru: 'Неоновая Казна', d_ru: 'Сохраните 500 Rc.', r_ru: 'Банкир', pt: 'Tesouro Neon', d_pt: 'Mantenha pelo menos 500 Rc simultaneamente.', r_pt: 'Banqueiro', check:")
    if "elite_hunter" in line: return line.replace("check:", "fr: 'Chasseur d\\'Élite', d_fr: 'Éliminez 10 unités d\\'Élite.', r_fr: 'Chasseur', ru: 'Охотник на Элиту', d_ru: 'Уничтожьте 10 Элитных врагов.', r_ru: 'Охотник', pt: 'Caça-Elites', d_pt: 'Elimine 10 inimigos Elite em uma incursão.', r_pt: 'Caçador', check:")
    if "level_5" in line: return line.replace("check:", "fr: 'Dôme Intouchable', d_fr: '500 élimin. sans dégâts sur le Noyau.', r_fr: 'Commandant', ru: 'Неприкасаемый Купол', d_ru: '500 убийств без урона ядру.', r_ru: 'Командир', pt: 'Cúpula Intocável', d_pt: '500 abates sem o Núcleo receber danos.', r_pt: 'Comandante', check:")
    if "boss_slayer" in line: return line.replace("check:", "fr: 'Tueur de Géants', d_fr: 'Assistez à la destruction d\\'un Boss.', r_fr: 'Légende', ru: 'Убийца Гигантов', d_ru: 'Уничтожьте первого Босса.', r_ru: 'Легенда', pt: 'Matador Cósmico', d_pt: 'Veja a destruição do primeiro Chefe.', r_pt: 'Lenda', check:")
    if "void_commander" in line: return line.replace("check:", "fr: 'Commandant du Vide', d_fr: 'Dépassez 2000 éliminations.', r_fr: 'Mythe', ru: 'Командир Пустоты', d_ru: 'Превысьте 2000 убийств.', r_ru: 'Миф', pt: 'Comandante Vazio', d_pt: 'Ultrapasse 2000 abates.', r_pt: 'Mito', check:")
    if "wave_15" in line: return line.replace("check:", "fr: 'Vétéran de Guerre', d_fr: 'Résistez jusqu\\'à la Vague 15.', r_fr: 'Vétéran', ru: 'Ветеран Войны', d_ru: 'Доживите до 15 Войны.', r_ru: 'Ветеран', pt: 'Veterano', d_pt: 'Resista até a Onda 15.', r_pt: 'Veterano', check:")
    if "rich_boy" in line: return line.replace("check:", "fr: 'Magnat de l\\'Énergie', d_fr: 'Cumulez 1500 Rc.', r_fr: 'Magnat', ru: 'Магнат Энергии', d_ru: 'Накопите 1500 Rc.', r_ru: 'Магнат', pt: 'Magnata da Energia', d_pt: 'Acumule 1500 Rc.', r_pt: 'Magnata', check:")
    if "rc_hoarder" in line: return line.replace("check:", "fr: 'Accumulateur', d_fr: 'Gardez jalousement 3000 Rc.', r_fr: 'Collectionneur', ru: 'Накопитель', d_ru: 'Накопите 3000 Rc.', r_ru: 'Коллекционер', pt: 'Acumulador', d_pt: 'Guarde 3000 Rc sem gastar.', r_pt: 'Colecionador', check:")
    if "rc_singularity" in line: return line.replace("check:", "fr: 'Singularité', d_fr: 'Devenez une source avec 5000 Rc.', r_fr: 'Étoile', ru: 'Сингулярность', d_ru: 'Соберите 5000 Rc.', r_ru: 'Звезда', pt: 'Singularidade', d_pt: 'Transforme-se com 5000 Rc.', r_pt: 'Estrela', check:")
    if "combo_25" in line: return line.replace("check:", "fr: 'Carnage Néon', d_fr: 'Atteignez un Combo x25.', r_fr: 'Bourreau', ru: 'Неоновая Резня', d_ru: 'Достигните Комбо x25.', r_ru: 'Палач', pt: 'Carnificina Neon', d_pt: 'Alcance um Combo x25.', r_pt: 'Carrasco', check:")
    if "max_orbs" in line: return line.replace("check:", "fr: 'Architecte', d_fr: 'Maintenez 10 orbes déployés.', r_fr: 'Architecte', ru: 'Архитектор', d_ru: 'Держите 10 сфер активными.', r_ru: 'Архитектор', pt: 'Arquiteto', d_pt: 'Mantenha 10 orbes ativos simultaneamente.', r_pt: 'Arquiteto', check:")
    if "max_gravs" in line: return line.replace("check:", "fr: 'Seigneur', d_fr: 'Créez 4 gravitons.', r_fr: 'Contrôleur', ru: 'Повелитель', d_ru: 'Создайте 4 гравитона.', r_ru: 'Контроллер', pt: 'Senhor da Gravidade', d_pt: 'Crie 4 gravitons ativos.', r_pt: 'Controlador', check:")
    if "elite_massacre" in line: return line.replace("check:", "fr: 'Exterminateur', d_fr: 'Liquidez 50 Drones Élite.', r_fr: 'Chasseur', ru: 'Истребитель', d_ru: 'Уничтожьте 50 Элитных.', r_ru: 'Охотник', pt: 'Exterminador', d_pt: 'Liquide 50 Inimigos de Elite.', r_pt: 'Caçador', check:")
    if "god_slayer" in line: return line.replace("check:", "fr: 'Fléau Divin', d_fr: 'Détruisez 3 Boss Massifs.', r_fr: 'Divinité', ru: 'Бич Богов', d_ru: 'Уничтожьте 3 Босса.', r_ru: 'Божество', pt: 'Açougueiro', d_pt: 'Destrua 3 Chefes Massivos.', r_pt: 'Divindade', check:")
    if "void_god" in line: return line.replace("check:", "fr: 'Dieu du Vide', d_fr: 'Annihilez 4000 ennemis.', r_fr: 'Dieu', ru: 'Бог Пустоты', d_ru: 'Уничтожьте 4000 врагов.', r_ru: 'Бог', pt: 'Deus do Vazio', d_pt: 'Aniquile 4000 inimigos.', r_pt: 'Deus', check:")
    if "void_entity" in line: return line.replace("check:", "fr: 'Entité Cosmique', d_fr: 'Atteignez 7500 éliminations.', r_fr: 'Transcendant', ru: 'Космическая Сущность', d_ru: 'Достигните 7500 убийств.', r_ru: 'Превосходный', pt: 'Entidade Cósmica', d_pt: 'Alcance 7500 abates.', r_pt: 'Transcendente', check:")
    return line

text = re.sub(r'\{ id: [^\}]+\},', replace_ach, text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Translations applied successfully.")
