"""Canonical research participants; affiliation, hosting and direction stay distinct."""
from collections import Counter


def build_actors(spec, works, industry):
    actors = {x['id']: dict(x) for x in spec['actors']}
    aliases = {}
    for a in actors.values():
        for label in dict.fromkeys(a['aliases']+[a['name']]):
            assert label not in aliases, label
            aliases[label] = [a['id']]
    aliases.update(spec['alias_expansions'])
    profiles = {a['profile_id']: a['id'] for a in actors.values() if a.get('profile_id')}
    for w in works:
        participants = {}

        def bind(aid, label, role, url):
            assert aid in actors, aid
            p = participants.setdefault(aid, {'actor_id': aid, 'raw_labels': [], 'roles': [], 'sources': []})
            for key, value in [('raw_labels', label), ('roles', role), ('sources', url)]:
                if value and value not in p[key]:
                    p[key].append(value)

        for label in w['organizations']:
            assert label in aliases, f'Classify new affiliation: {label}'
            for aid in aliases[label]:
                bind(aid, label, 'joint_lab' if label in spec['alias_expansions'] else 'affiliation', w['team_source'])
        for aid in spec.get('work_overrides', {}).get(w['id'], []):
            bind(aid, w['team'], 'project_team', w['team_source'])
        for c in industry['companies']:
            for link in c['work_links']:
                if link['work_id'] == w['id'] and link['relationship'] != 'hosted':
                    bind(profiles[c['id']], '', link['relationship'], link['source_url'])
        w['participants'] = list(participants.values())
        w['actor_ids'] = list(participants)
        kinds = set(actors[x]['kind'] for x in participants)
        w['actor_types'] = sorted(kinds or {'unresolved'})
        named = [x for x in participants if actors[x].get('countable', True)]
        if 'academic' in kinds and kinds & {'tech', 'ai'}:
            cooperation = 'academic_industry'
        elif len(named) > 1:
            cooperation = 'multi_org'
        elif not named or kinds <= {'unresolved'}:
            cooperation = 'unresolved'
        else:
            cooperation = 'single'
        w['cooperation'] = cooperation
    for a in actors.values():
        a['work_ids'] = [w['id'] for w in works if a['id'] in w['actor_ids']]
    return {**spec, 'actors': list(actors.values()),
            'counts': dict(Counter(a['kind'] for a in actors.values() if a.get('countable', True)))}
