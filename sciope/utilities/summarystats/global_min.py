# Copyright 2019 Prashant Singh, Fredrik Wrede and Andreas Hellander
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The global minimum summary statistic
"""

# Imports
import numpy as np
from sciope.utilities.summarystats.summary_base import SummaryBase
from sciope.utilities.housekeeping import sciope_logger as ml


# Class definition: Global Min Statistic
class GlobalMin(SummaryBase):
    """
    The minimum value observed across the entire time span
    """

    def __init__(self, mean_trajectories=True, use_logger=True):
        self.name = 'GlobalMin'
        super(GlobalMin, self).__init__(self.name, mean_trajectories, use_logger)
        if self.use_logger:
            self.logger = ml.SciopeLogger().get_logger()
            self.logger.info("GlobalMin summary statistic initialized")

    def compute(self, data):
        """
        Calculate the value(s) of the summary statistic(s)
        :param data: simulated or data set
        :return: computed statistic value
        """
        if self.mean_trajectories:
            res = np.asarray(np.mean(np.min(data, axis=1)))  # returns a scalar
        else:
            res = np.min(data, axis=1)  # returns a np array

        res = np.reshape(res, (res.size, 1))  # reshape to proper dimensions

        if self.use_logger:
            self.logger.info("GlobalMin summary statistic: processed data matrix of shape {0} and generated summaries"
                             " of shape {1}".format(data.shape, res.shape))
        np.testing.assert_equal(res.shape[0], data.shape[0], "GlobalMin: expected summaries count mismatch!")
        return res