import logging

from view.yobit_defi_view import YobitDefiView


class YobitDefiController:
    def __init__(self, model, log_name="yobit_defi"):
        self._logger = logging.getLogger(f'{log_name}.controller')

        self._model = model

        self._view = YobitDefiView(self, model, log_name)

        self._view.show()

    def set_pair(self):
        try:
            pair = self._view.ui.pair_cmbox.currentText()
            self._model.pair = pair
        except Exception:
            self._logger.exception('Ошибка при попытке считать комбобокс с парами')
        else:
            self._logger.info(f'В программу введена пара: {pair}')

    def set_arbitrage(self):
        try:
            arbitrage = float(self._view.ui.arbitrage_ledit.text())
            self._model.arbitrage = arbitrage
        except:
            self._logger.error('Введите арбитраж числом')
        else:
            self._logger.info(f'В программу введен арбитраж: {arbitrage}')
