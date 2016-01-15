# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.cluster.v1 import cluster_policy


FAKE = {
    'cluster_id': '99e39f4b-1990-4237-a556-1518f0f0c9e7',
    'cluster_name': 'test_cluster',
    'data': {'purpose': 'unknown'},
    'enabled': True,
    'id': 'c378e474-d091-43a3-b083-e19719291358',
    'policy_id': 'ac5415bd-f522-4160-8be0-f8853e4bc332',
    'policy_name': 'dp01',
    'policy_type': 'senlin.poicy.deletion-1.0',
}


class TestClusterPolicy(testtools.TestCase):

    def setUp(self):
        super(TestClusterPolicy, self).setUp()

    def test_basic(self):
        sot = cluster_policy.ClusterPolicy()
        self.assertEqual('cluster_policy', sot.resource_key)
        self.assertEqual('cluster_policies', sot.resources_key)
        self.assertEqual('policy_id', sot.id_attribute)
        self.assertEqual('/clusters/%(cluster_id)s/policies',
                         sot.base_path)
        self.assertEqual('clustering', sot.service.service_type)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_list)

    def test_instantiate(self):
        sot = cluster_policy.ClusterPolicy(FAKE)
        self.assertEqual(FAKE['policy_id'], sot.id)
        self.assertEqual(FAKE['cluster_id'], sot.cluster_id)
        self.assertEqual(FAKE['cluster_name'], sot.cluster_name)
        self.assertEqual(FAKE['data'], sot.data)
        self.assertEqual(FAKE['enabled'], sot.enabled)
        self.assertEqual(FAKE['policy_id'], sot.policy_id)
        self.assertEqual(FAKE['policy_name'], sot.policy_name)
        self.assertEqual(FAKE['policy_type'], sot.policy_type)