class Match:
  def __init__(self, tds):
    raise NotImplementedError("Subclass must implement abstract method")


class SfstatsMatch(Match):
  def __init__(self, tds):
    self.home_team_name = tds[0].get_text()
    self.away_team_name = tds[1].get_text()
    self.home_rate = float(tds[2].get_text())
    self.draw_rate = float(tds[3].get_text())
    self.away_rate = float(tds[4].get_text())


class VitisportMatch(Match):
  def __init__(self, tds):
    self.home_team_name = tds[2].get_text()
    self.away_team_name = tds[3].get_text()
    self.home_rate = calc_rate(tds[8].get_text().split()[0])
    self.draw_rate = calc_rate(tds[9].get_text().split()[0])
    self.away_rate = calc_rate(tds[10].get_text().split()[0])


class WdwMatch(Match):
  def __init__(self, soup):
    # Team name data extraction
    self.team_name_home = soup.select('#content > div > div > div.teambox > div > div.tbtr.darkrow > div')[0].get_text()
    self.team_name_away = soup.select('#content > div > div > div.teamboxright > div > div.tbtr.darkrow > div')[0].get_text()

    # Predictions data extraction
    predictions = soup.select_one('#content > div > div > div.tbtr.mb30.bgwht > div.contenthalf1 > div.compareoddswrapper > div.tbtr.pt10.pb10 > div')
    self.home = predictions.select('div.tbtr')[0].select('div')[3].get_text().split("%")[0]
    self.draw = predictions.select('div.tbtr')[1].select('div')[3].get_text().split("%")[0]
    self.away = predictions.select('div.tbtr')[2].select('div')[3].get_text().split("%")[0]

    # Stake data extraction
    stake_text_split = soup.select_one('#content > div > div > div.tbtr.mb30.bgwht > div.contenthalf1 > div.featuretipwrapper > div.tbtd2.w100p.featuretip').get_text().split(" on")
    self.stake_rate = stake_text_split[0]
    self.stake_result = stake_text_split[1]

    # Result data extraction
    result_text_split = soup.select_one('#content > div > div > div.tbtr.mb30.bgwht > div.contenthalf1 > div.featuretipwrapper > div.tbtd2.w100p.featurescore').get_text().split("-")
    self.home_result = result_text_split[0]
    self.away_result = result_text_split[1]


def calc_rate(percent):
  return round(100 / float(percent), 2)
